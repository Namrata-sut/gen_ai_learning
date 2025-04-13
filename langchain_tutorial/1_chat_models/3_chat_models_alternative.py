# past conversation history in next AI msg
import os

from langchain_community.chat_models import ChatOpenAI, ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from pyexpat.errors import messages

message = [
    SystemMessage("You are expert in social media content strategy"),
    HumanMessage("Give a short tip to create engaging posts on Instagram."),
    AIMessage("Use strong calls to action. Encourage interaction by asking questions,"
              " running polls, or prompting users to tag a friend. "
              " This transforms passive viewers into active participants."),

]

# LangChain Google model example

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#
# llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro', api_key=GEMINI_API_KEY)
#
# result = llm.invoke(message)
# print(result.content)

# LangChain OpenAI model example

# model = ChatOpenAI(model='gpt-4o')
#
# result = model.invoke(message)
# print(f"Answer from OpenAI: {result.content}")

# LangChain Anthropic model example

model = ChatAnthropic(model='claude-3-opus-20240229')

result = model.invoke(message)
print(f"Answer from OpenAI: {result.content}")
