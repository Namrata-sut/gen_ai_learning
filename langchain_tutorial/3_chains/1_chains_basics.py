import os

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=GEMINI_API_KEY)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a facts expert who knows facts about {animal}."),
    ("human", "Tell me {fact_count} facts."),
])

# create combined chain using LangChain expression Language
chain = prompt_template | llm | StrOutputParser()

# Run the chain
result = chain.invoke({
    "animal": "cat", "fact_count": 2
})

print(result)
