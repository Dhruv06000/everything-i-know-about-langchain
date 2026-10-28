from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-fable-5-1')
result = model.invoke("What is the capital of india ?")

print(result.content)
