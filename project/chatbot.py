from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

chatHistory = [
    SystemMessage(content="You are a helpful AI assistent and answer the questions patiently")

]


while(True):
    user_ip = input('You: ')
    chatHistory.append(HumanMessage(content=user_ip)) 
    if(user_ip == 'exit'):
        print(chatHistory)
        break
    else:
        result = model.invoke(chatHistory)
        chatHistory.append(AIMessage(content=result.content))
        print("AI:",result.content)
