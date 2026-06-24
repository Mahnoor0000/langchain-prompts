from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    SystemMessage(content='You are a helpful assistant!'),
    HumanMessage(content='Tell me about langchain'),

]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)