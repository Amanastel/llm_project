from langchain.llms import OpenAI


llm = OpenAI(openai_api_key="...",temperature=0.3)


print(llm.predict("what is capital of india"))