from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = HuggingFacePipeline.from_model_id(
  model_id = "Qwen/Qwen2.5-3B-Instruct",
  task = "text-generation",
  pipeline_kwargs=dict(
    temperature=0.5,
    do_sample=True,
    return_full_text=False,
  )
)
model = ChatHuggingFace(llm=llm)

prompt_1 = PromptTemplate(
  template = 'Generate a detailed report on {topic}',
  input_variables = ['topic']
)

prompt_2 = PromptTemplate(
  template = 'Generate a 5 pointer summary from the following text \n {text}',
  input_variables = ['text']
)


parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({'topic' : 'Unemployment in the India'})

print(result)

chain.get_graph().print_ascii()