
import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain.chains import create_sql_query_chain
import re

from connection import db_query

load_dotenv()

# Define your local PostgreSQL connection string
db = SQLDatabase.from_uri("postgresql://postgres:sigdel@localhost:8080/db_phone")

# Load the LLM (Groq's Llama 3.3)
models = ["gemma2-9b-it","llama-3.3-70b-versatile"]
llm = ChatGroq(model_name= models[0]) 

# Create the SQL query chain
query_chain = create_sql_query_chain(llm, db)

#create a question
question = "Name 5 phone models?"

# Test with a natural language question
query_response = query_chain.invoke({"question": question})

#use regex to extract the sql query.
match = re.search(r"SQLQuery:\s*(.+)", query_response, re.DOTALL)

if match:
    sql_query = match.group(1).strip()
else:
    sql_query = "No query found"
sql_query = sql_query.replace('`', '')

# Print the query
print(sql_query)
print("\n")

#query the db
rows = db_query(sql_query)

#formating the output
if len(rows) != 1:
    # print the answers
    for row in rows:
        print(f"{row} ")
else:
    row = rows[0][0]
    print(row)