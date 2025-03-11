# DDL commands come in the following types: CREATE, ALTER, DROP, RENAME, and TRUNCATE
# DML commands come in the following types: SELECT, INSERT, UPDATE, DELETE, and MERGE
import psycopg2 as pg
import psycopg2.extras as pgx
from config_loader import load_config

#load the database configuration
db_config = load_config()
hostname,dbname,user,password,port = db_config.values()

# handling emptiness for conn and cur 
conn = None
cur = None

def db_query(query):
    # create a connection
    ##can use with clause for auto closing connection. with allows auto commit.
    try:
        conn = pg.connect(
            host = hostname,
            dbname = dbname,
            user = user,
            password = password,
            port = port
        )
        cur = conn.cursor()
        # cur = conn.cursor(cursor_factory=pgx.DictCursor)

        #execute the query
        cur.execute(query)
        
        #store the result in rows 
        rows = cur.fetchall()

        #commiting the DML back to database
        conn.commit()

    #catch an exception
    except Exception as error:
        print(error)

    # if there is cur and conn close them
    finally:
        if cur is not None: cur.close()
        if conn is not None: conn.close()

    #return the result
    return rows

###provide the query
query = """
select id,brand,model,price from tbl_phones
where price < 500
"""
###
# print(db_query(query))



"""
insert_script = 'INSERT INTO tbl_phone(brand, model, price) VALUES (%s,%s,%s)
insert_values = [('DamDum','Note','450.00'),('DamDum','Note2','470.00'),('DamDum','Note 5','599.99')]

for record in insert_values:
    cur.execute(insert_script,record)
"""

"""
        #fetch all data
        for row in cur.fetchall():
            id,brand, model, price = row
            print(f"Brand: {brand}, Model:\"{model}\", Price: {price}")
"""
"""
        # cur = conn.cursor(cursor_factory=pgx.DictCursor)
        # for row in cur.fetchall():
        #     print(f"Brand:{row['brand']},  Model:{row['model']},  Price:{float(row['price'])}  ")
"""