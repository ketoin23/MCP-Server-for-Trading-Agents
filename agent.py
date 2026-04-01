from smolagents import ToolCallingAgent, ToolCollection, LiteLLMModel
from mcp import StdioServerParameters

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5:7b",
    num_ctx=8192
)

server_parameters = StdioServerParameters(
    command="uv",
    args=["run", "server.py"],
    env=None,
)

with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
    strict_prompt = """Who are the core leaders at Walmart?
    
    CRITICAL: You must respond with ONLY the raw JSON tool call. 
    Do not include any conversational text before or after. 
    Do not wrap the response in markdown code blocks. 
    Your entire response must start with { and end with }."""
    
    agent.run(strict_prompt)