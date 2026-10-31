# List of Messages - Static Conversation (Fixed list of SystemMessage, HumanMessage, AIMessage)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= "gpt-4o-mini")

messages = [
  SystemMessage(content="You are a helpful Assistent."),
  HumanMessage(content="Tell me about python")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

