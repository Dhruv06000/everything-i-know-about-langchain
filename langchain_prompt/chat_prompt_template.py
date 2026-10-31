# List of Messages - Dynamic Template using ChatPromptTemplate

# Below will not work due to LangChain weird behaviour due to having new framework 

# from langchain_core.prompts import ChatPromptTemplate 
# from langchain_core.messages import SystemMessage , HumanMessage

# chat_template = ChatPromptTemplate([
#   SystemMessage(content='You are a helpful {domain} expert'),
#   HumanMessage(content='Explain in simple terms, what is {topic}')
# ])

# prompt = chat_template.invoke({
#   'domain':'cricket',
#   'topic':'Dusra'})
# print(prompt)

# Output : messages=[SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is {topic}', additional_kwargs={}, response_metadata={})]

from langchain_core.prompts import ChatPromptTemplate 

# chat_template = ChatPromptTemplate.from_messages([])
# or 
chat_template = ChatPromptTemplate([

  ('system','You are a helpful {domain} expert'),
  ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({
  'domain':'cricket',
  'topic':'Dusra'})
print(prompt)