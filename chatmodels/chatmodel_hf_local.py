from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='sentence-transformers/all-MiniLM-L6-v2',
    task = 'text-generation',
)

model = ChatHuggingFace(llm=llm)
query = input("Enter Your query: ")
result = model.invoke(f"{query}")
print(result.content)