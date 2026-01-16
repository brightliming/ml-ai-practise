from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model = "deepseek-chat",
    api_key="1234",
    base_url="https//api.deepseek.com/v1",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_template("you are a {role},please anwser :{question}")

chain = prompt | llm

response = chain.invoke({"role":"AI expert","question":"can Langchain integrate with Deepseek?"})

print(response.content)
