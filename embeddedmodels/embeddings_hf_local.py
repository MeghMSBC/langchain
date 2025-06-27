from langchain_huggingface import HuggingFaceEmbeddings
import os 

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = [
    "Delhi is the capital of india",
    "Gujarat is in the west",
    "kolkata is in the east"
]

vector = embedding.embed_documents(text)

print(str(vector))
