import os
import datetime
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents import tool
# load_dotenv()

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current date and time in the specified format."""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=GEMINI_API_KEY)

# query = "What is the current time?"
# query = "What is the current time? Just show the current time and not the date."
query = "What is the current time in London (You are in India)? Just show the current time and not the date."
prompt_template = hub.pull("hwchase17/react")
# https://smith.langchain.com/hub/hwchase17/react
tools = [get_system_time]

agent = create_react_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
result = agent_executor.invoke({"input": query})
print(result)


