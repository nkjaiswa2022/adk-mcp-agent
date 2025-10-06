import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, \
                StdioServerParameters, StdioConnectionParams
from dotenv import load_dotenv

load_dotenv()
google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

if not google_maps_api_key:
    print("WARNING: GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable or update it in the script.")

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.',

    ## Add the MCPToolset below:
)