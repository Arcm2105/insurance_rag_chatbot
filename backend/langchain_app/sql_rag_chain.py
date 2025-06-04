import os
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load keys
load_dotenv()

# SQLite DB Path
db = SQLDatabase.from_uri("sqlite:///data/insurance_data.db")

# LLM Model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Toolkit for SQL interaction
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)