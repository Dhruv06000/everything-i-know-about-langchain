from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = model.invoke("Write a one-sentence story about a fish that is afraid of water.")

print(result)
