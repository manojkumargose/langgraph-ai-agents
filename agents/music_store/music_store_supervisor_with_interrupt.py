from agents.music_store.music_store_supervisor import supervisor
from utils.models import model
from utils.utils import get_engine_for_chinook_db

from langgraph.graph import StateGraph, START, END
from typing import Annotated, Optional, NotRequired
from langgraph.graph.message import AnyMessage, add_messages
from langgraph.managed.is_last_step import RemainingSteps
from typing_extensions import TypedDict
from langchain.messages import SystemMessage, HumanMessage
import ast
from langchain_community.utilities.sql_database import SQLDatabase
from pydantic import BaseModel, Field
from langgraph.types import interrupt

engine = get_engine_for_chinook_db()
db = SQLDatabase(engine)


class InputState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


class State(InputState):
    customer_id: NotRequired[str]
    loaded_memory: NotRequired[str]
    remaining_steps: NotRequired[RemainingSteps]


class UserInput(BaseModel):
    """Schema for parsing user-provided account information."""
    identifier: str = Field(description="Identifier, which can be a customer ID, email, or phone number.")


structured_llm = model.with_structured_output(schema=UserInput)
structured_system_prompt = """You are a customer service representative responsible for extracting customer identifier.
Only extract the customer's account information from the message history.
If they haven't provided the information yet, return an empty string for the field."""


def get_customer_id_from_identifier(identifier: str) -> Optional[int]:
    """Retrieve Customer ID using a customer ID, email, or phone number."""
    identifier = identifier.strip()
    if not identifier:
        return None
    if identifier.isdigit():
        return int(identifier)
    elif identifier[0] == "+":
        query = f"SELECT CustomerId FROM Customer WHERE Phone = '{identifier}';"
        result = db.run(query)
        formatted_result = ast.literal_eval(result) if result else []
        if formatted_result:
            return formatted_result[0][0]
    elif "@" in identifier:
        query = f"SELECT CustomerId FROM Customer WHERE Email = '{identifier}';"
        result = db.run(query)
        formatted_result = ast.literal_eval(result) if result else []
        if formatted_result:
            return formatted_result[0][0]
    return None


# Node
def verify_info(state: State):
    """Verify the customer's account by parsing their input and matching it with the database."""

    # Already verified -> nothing to do
    if state.get("customer_id") is not None:
        return {}

    system_instructions = """You are a music store agent, where you are trying to verify the customer identity
    as the first step of the customer support process.
    Only after their account is verified, you would be able to support them on resolving the issue.
    In order to verify their identity, one of their customer ID, email, or phone number needs to be provided.
    If the customer has not provided their identifier, please ask them for it.
    If they have provided the identifier but cannot be found, please ask them to revise it."""

    user_input = state["messages"][-1]

    # Parse for customer identifier
    parsed_info = structured_llm.invoke(
        [SystemMessage(content=structured_system_prompt), user_input]
    )
    identifier = parsed_info.identifier

    customer_id = None
    if identifier:
        customer_id = get_customer_id_from_identifier(identifier)

    if customer_id is not None:
        # Do NOT add an AI message here: Gemini needs the last message to be from the user
        return {"customer_id": customer_id}

    response = model.invoke([SystemMessage(content=system_instructions)] + state["messages"])
    return {"messages": [response]}


# Node
def human_input(state: State):
    """No-op node that should be interrupted on."""
    user_input = interrupt("Please provide input.")
    if not str(user_input).strip():
        user_input = "I have not provided my details yet."  # avoids empty content error
    return {"messages": [HumanMessage(content=user_input)]}


# Conditional edge
def should_interrupt(state: State):
    if state.get("customer_id") is not None:
        return "continue"
    else:
        return "interrupt"


# Build graph
multi_agent_verify = StateGraph(State, input_schema=InputState)
multi_agent_verify.add_node("verify_info", verify_info)
multi_agent_verify.add_node("human_input", human_input)
multi_agent_verify.add_node("supervisor", supervisor)

multi_agent_verify.add_edge(START, "verify_info")
multi_agent_verify.add_conditional_edges(
    "verify_info",
    should_interrupt,
    {
        "continue": "supervisor",
        "interrupt": "human_input",
    },
)
multi_agent_verify.add_edge("human_input", "verify_info")
multi_agent_verify.add_edge("supervisor", END)
graph = multi_agent_verify.compile(name="multi_agent_verify")