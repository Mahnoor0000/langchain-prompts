from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert!'),
    ('human','explain in simple terms, what is {topic}') 
])

prompt = chat_template.invoke({'domain':'cricket','topic':'pitch'})

print(prompt)