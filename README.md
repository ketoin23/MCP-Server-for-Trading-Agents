# MCP Trading

An AI-powered financial analysis agent that leverages the Model Context Protocol (MCP) to provide intelligent trading insights and stock market analysis.

## Overview

MCP Trading is a sophisticated system that combines:
- **Financial Data Tools**: Real-time and historical stock market data via Yahoo Finance
- **AI Agent**: An intelligent tool-calling agent powered by open-source LLMs
- **Model Context Protocol**: Standardized communication between the agent and financial data sources
- **Local LLM Support**: Uses Ollama with Qwen2.5 for privacy-preserving analysis

The system enables you to ask natural language questions about stocks and companies, with the AI agent automatically selecting and using the appropriate financial tools to gather data and provide answers.

## Architecture

```
┌─────────────────────────────────┐
│   Agent (LLM Interface)         │
│   - Tool-calling agent          │
│   - LiteLLM Model Integration   │
└──────────────┬──────────────────┘
               │
        MCP Protocol
               │
┌──────────────▼──────────────────┐
│   MCP Server                    │
│   - Stock Price Tool            │
│   - Stock Info Tool             │
│   - Income Statement Tool       │
└──────────────┬──────────────────┘
               │
               │
┌──────────────▼──────────────────┐
│   Yahoo Finance (yfinance)      │
│   - Market Data                 │
│   - Company Information         │
│   - Financial Statements        │
└─────────────────────────────────┘
```

## Features

### Available Tools

1. **Stock Price** (`stock_price`)
   - Retrieves the last known price and 1-month historical closing prices for a given stock ticker
   - Example: `NVDA` returns price data for NVIDIA

2. **Stock Information** (`stock_info`)
   - Returns comprehensive company information including address, industry, website, and more
   - Example: `IBM` returns IBM's corporate details

3. **Income Statement** (`income_statement`)
   - Fetches quarterly income statements for financial analysis
   - Example: `BOA` returns Bank of America's quarterly financial data

### AI Agent Capabilities

The agent can:
- Understand natural language financial queries
- Automatically select appropriate tools to answer questions
- Combine multiple data sources for comprehensive analysis
- Provide insights about company leadership, performance, and financial health

## Setup

### Requirements

- Python 3.12+
- Ollama (with Qwen2.5 model)
- uv (for running the MCP server)

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
# or
uv sync
```

### Configuration

The project is configured via `pyproject.toml`. Key dependencies:
- `smolagents[mcp]` - AI agent framework with MCP support
- `yfinance` - Yahoo Finance data provider
- `fastmcp` - Fast MCP server implementation
- `litellm` - LLM abstraction layer
- `colorama` - Terminal color output

## Usage

### Running the Agent

```bash
python agent.py
```

This will start the tool-calling agent with a Qwen2.5 LLM (via Ollama) and execute a sample query about Walmart's leadership.

### Running the Server Only

```bash
uv run server.py
```

This starts the MCP server on stdio, providing financial data tools to connected clients.

### Custom Queries

Modify the `strict_prompt` variable in `agent.py` to ask different questions:

```python
strict_prompt = """Your financial question here"""
agent.run(strict_prompt)
```

## Dependencies

- **smolagents**: Open-source agent framework for tool calling
- **yfinance**: Yahoo Finance Python library for market data
- **fastmcp**: High-performance MCP server implementation
- **litellm**: Universal LLM interface supporting multiple providers
- **mcp[cli]**: Model Context Protocol specification and CLI tools
- **colorama**: Cross-platform terminal colors
- **ollama_chat backend**: Local inference using Ollama

## Project Structure

```
mcp-trading/
├── agent.py           # Tool-calling agent with LLM integration
├── server.py          # MCP server with financial tools
├── main.py            # Entry point
├── pyproject.toml     # Project configuration and dependencies
└── README.md          # This file
```

## How It Works

1. **User Query**: A natural language financial question is provided to the agent
2. **Tool Selection**: The agent analyzes the query and decides which financial tools to use
3. **Data Collection**: The MCP server tools interact with Yahoo Finance to gather data
4. **Analysis**: The agent processes the retrieved data with the LLM
5. **Response**: The user receives an AI-generated answer with relevant financial insights

## Example Query

```
Agent: "Who are the core leaders at Walmart?"
↓
Agent selects: stock_info("WMT")
↓
Server queries: Yahoo Finance for WMT information
↓
Response: Returns company details including leadership information
```

## Requirements

See `pyproject.toml` for the complete dependency list. Core requirements:
- Python 3.12+
- Ollama with Qwen2.5 model running locally

## Future Enhancements

- Support for additional financial metrics and analysis tools
- Integration with more LLM providers
- Advanced portfolio analysis capabilities
- Real-time alerts and notifications
- Historical trend analysis
- Comparative company analysis
