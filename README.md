# PostgreSQL Access with Python

This project provides a structured approach to accessing a PostgreSQL database using Python 3.11. It utilizes various libraries to handle database connections, queries, and natural language interactions.
N.B: This is just a practice project. Learning chains and agents and how they work.

## Features
- Secure credential management using `config.ini`
- Database connection and querying via `psycopg2`
- Query execution and response retrieval using `db_query`
- SQL generation using `query_chain.py`
- Natural language database interactions via `query_agent.py`

## Installation

### Prerequisites
Ensure you have Python 3.11 installed on your system.

### Install Dependencies
Copy the text in install.txt file and paste in the terminal. I find this more effective than requirements.txt method.

## Project Structure

```
├── config.ini          # Stores database credentials
├── install.txt         # Contains required libraires
├── config_loader.py    # Loads database credentials
├── connection.py       # Establishes database connection
├── query_chain.py      # Generates SQL queries through chains
├── query_agent.py      # Provides natural language responses through agent
```

## Configuration

Update the `config.ini` file with your database credentials:
```ini
[database]
host = your_host
database = your_database
user = your_username
password = your_password
port = your_port
```

## Author
Developed by [Vishal Sigdel](https://github.com/Page-Vishal)

