import os
from http.client import responses

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.schema import AIMessage, HumanMessage, SystemMessage

# load enviroment variables from .env
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# create a ChatGoogleGenerativeAI model.
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=GEMINI_API_KEY)

chat_history = [] # use a list to store messages

# set an initial system message(optional)
system_message = SystemMessage(content='You are a helpful AI assistant.')
chat_history.append(system_message) # add system message

# chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query)) # add user message

    # Gen AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) # add AI message

    print(f"AI: {response}")

print("----message history----")
print(chat_history)


