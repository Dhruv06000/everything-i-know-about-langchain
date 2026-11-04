from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini",temperature=0.1,max_completion_tokens=11)

result = model.invoke("Write a one-sentence story about a fish that is afraid of water.")

print(result.content)