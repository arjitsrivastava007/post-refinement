from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4")
