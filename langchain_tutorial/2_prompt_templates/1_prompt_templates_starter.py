import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key = GEMINI_API_KEY)

# template = ("Write a {tone} email to {company} expressing interest in the "
#             "{position} position, mentioning  {skill} as a key strength. "
#             "Keep it to 4 lines max.")
#
# prompt_template = ChatPromptTemplate.from_template(template)
# print(f"----------{prompt_template}----------------")
#
# prompt = prompt_template.invoke({
#     "tone": "energetic",
#     "company": "samsung",
#     "position": "AI Engineer",
#     "skill": "AI"
# })
#
# print(f"---------------------{prompt}------------------")
#
# result = llm.invoke(prompt)
#
# print(f"-----{result.content}-------")

messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})

print("\n----- Prompt with system and human messages (Tuple) ------\n")
print(prompt)

result = llm.invoke(prompt)

print(f"-------{result.content}------")
