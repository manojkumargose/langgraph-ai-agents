# LangGraph 101 — AI Agents and Workflows

Welcome to LangGraph 101!

## Introduction

This repository contains hands-on tutorials and implementations for learning LangChain, LangGraph, and Deep Agents. It covers fundamental agent development concepts as well as advanced patterns for building multi-agent systems and production workflows.

The project explores two learning tracks:

* **101 — Fundamentals:** Building AI agents using LangChain and LangGraph.
* **201 — Advanced Patterns:** Multi-agent systems, Deep Agents, and production-oriented workflows.

To understand how these frameworks relate to each other, see the [LangChain vs LangGraph vs Deep Agents documentation](https://docs.langchain.com/oss/python/concepts/products).

For additional tutorials and guided learning, visit [LangChain Academy](https://academy.langchain.com/courses/intro-to-langgraph).

## Key Features

* AI agent development using LangChain and LangGraph.
* Tool integration and tool-calling workflows.
* Stateful agent workflows and memory.
* Human-in-the-loop interaction patterns.
* Multi-agent systems with supervisors and specialized subagents.
* Deep research workflows with parallel sub-researchers.
* Deep Agents with skills, memory, and configurable instructions.
* Local development and debugging using LangGraph Studio.
* Configurable language model providers.

## Project Structure

```text
langgraph-ai-agents/
├── agents/
│   ├── 101/
│   ├── deep_agent/
│   ├── email_agent/
│   ├── music_store/
│   └── researcher/
├── images/
├── mcp/
│   └── email_tools.py
├── notebooks/
│   ├── 101/
│   └── 201/
├── utils/
│   ├── models.py
│   └── utils.py
├── .env.example
├── .gitignore
├── langgraph.json
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## Technologies Used

* **Python** — Primary programming language.
* **LangChain** — Framework for building applications powered by language models.
* **LangGraph** — Framework for orchestrating stateful AI agent workflows.
* **Deep Agents** — Tools and patterns for building agents that handle complex, multi-step tasks.
* **Jupyter Notebook** — Interactive environment for learning and experimenting.
* **LangGraph CLI** — Local development and agent testing.
* **LLM providers** — Model integrations configured through the project utilities.

The exact model provider and required API keys depend on the configuration you choose.

## Agents

The repository contains several agent implementations:

### 1. Fundamentals Agent

Introduces basic agent functionality and demonstrates how an agent can interact with tools.

### 2. Email Agent

Explores stateful email triage and response workflows.

### 3. Music Store Multi-Agent System

Demonstrates a supervisor-based architecture in which specialized subagents can handle different tasks.

### 4. Research Agent

Explores research workflows that can delegate subtasks to parallel sub-researchers.

### 5. Deep Agent

Demonstrates advanced agent patterns, including configurable instructions, skills, memory, and human-in-the-loop interactions.

Refer to the source files and notebooks for each implementation's actual functionality.

## Getting Started

### Prerequisites

Install the following before starting:

* Python version supported by the project dependencies.
* Git.
* `uv` package manager.
* API credentials for your selected language model provider.

### 1. Clone the Repository

```bash
git clone https://github.com/manojkumargose/langgraph-ai-agents.git
cd langgraph-ai-agents
```

### 2. Create the Environment Configuration

Copy the example environment file:

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Linux or macOS:**

```bash
cp .env.example .env
```

Open `.env` and configure the required API keys for your selected provider.

**Security note:** Never commit `.env` or expose API keys publicly. The `.env.example` file should contain placeholders only.

### 3. Install Dependencies

Install `uv` if it is not already installed:

```bash
pip install uv
```

Install the project dependencies:

```bash
uv sync
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux or macOS:**

```bash
source .venv/bin/activate
```

### 5. Run the Agent Development Server

From the project root, run:

```bash
langgraph dev
```

This starts the local LangGraph development environment when the project and its configuration are correctly set up.

The CLI displays the available local endpoints and any relevant Studio access information.

## Model Configuration

The repository centralizes model configuration in `utils/models.py`.

Shared utility functions are located in `utils/utils.py`.

Depending on the implementation and installed dependencies, model configuration may support providers such as OpenAI, Anthropic, Azure OpenAI, Amazon Bedrock, or Google Vertex AI.

Before running an agent, check the relevant source file and configure the required provider credentials.

## Learning Path

A suggested learning path is:

1. Explore the introductory notebooks in `notebooks/101/`.
2. Learn about tools, state, memory, and agent workflows.
3. Explore middleware and human-in-the-loop patterns.
4. Study the email agent and multi-agent implementations.
5. Explore the research agent and Deep Agent implementations.
6. Run and test the agents locally using the LangGraph development tools.

## Useful Resources

* [LangChain Documentation](https://docs.langchain.com/oss/python/langchain/overview)
* [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
* [Deep Agents Documentation](https://docs.langchain.com/oss/python/deepagents/)
* [LangChain Academy](https://academy.langchain.com/)
* [LangGraph CLI Documentation](https://docs.langchain.com/langsmith/cli#langgraph-cli)

## Purpose

This repository serves as a practical learning environment for exploring AI agents, tool integration, workflow orchestration, and multi-agent architectures using Python and LangGraph.

**Note:** This repository builds on the LangGraph 101 learning materials. Review the source code and documentation to distinguish existing tutorial implementations from any modifications or extensions you make yourself.
