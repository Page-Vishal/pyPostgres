import os
import re
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit,create_sql_agent
from langchain_groq import ChatGroq

load_dotenv()
db = SQLDatabase.from_uri("postgresql://postgres:sigdel@localhost:8080/db_phone")
llm = ChatGroq(model_name= "gemma2-9b-it") 

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(llm,toolkit, verbose=True)

question = "Phones cheaper than 500 dollars. Show all the models"

response = agent_executor.invoke({"input": question})
print(response)