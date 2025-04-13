import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY, temperature=0.0)

# from langchain_google_vertexai import ChatVertexAI
#
# llm = ChatVertexAI(
#     model="gemini-1.5-flash-001",
#     temperature=0,
#     max_tokens=None,
#     max_retries=6,
#     stop=None
# )

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
# print("message: ", ai_msg)
print("content: ", ai_msg.content)

