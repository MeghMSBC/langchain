from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Magistral-Small-2506",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke()
print(result.content)