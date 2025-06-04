# backend/main.py

from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnableLambda
from backend.langchain_app.sql_rag_chain import agent_executor

app = FastAPI()

# ✅ Wrap agent_executor to avoid serialization issues
wrapped_chain = RunnableLambda(lambda x: agent_executor.invoke(x))

# ✅ Add route to serve the RAG chain
add_routes(app, wrapped_chain, path="/chat")