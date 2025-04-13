import os

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from dotenv import load_dotenv

# load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=GEMINI_API_KEY)

animal_fact_template = ChatPromptTemplate.from_messages([
    ("system", "You like telling facts and you tells facts about {animal}."),
    ("human", "Tell me {fact_count} facts."),
])

translatio_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}")
    ]
)

# Define additional processing steps using RunnableLambda
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})

# Create a combined chain using Langchain expression language (LCEL)
chain = animal_fact_template|llm|StrOutputParser()|prepare_for_translation|translatio_template|llm|StrOutputParser()

# Run the chain
result = chain.invoke({"animal": "cat", "fact_count": 2})

print(result)
