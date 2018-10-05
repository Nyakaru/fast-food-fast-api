import psycopg2
from models import connection

conn = connection()
cur = conn.cursor()

user_table = """
CREATE TABLE IF NOT EXISTS users(
    user_id serial PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR NOT NULL
   
    
);
"""

admin_table = """
CREATE TABLE IF NOT EXISTS admin(
    admin_id serial PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR NOT NULL
   
    
);
"""


meals_table = """
CREATE TABLE IF NOT EXISTS meals(
    meal_id serial PRIMARY KEY,
    price INTEGER NOT NULL,
    description VARCHAR NOT NULL,
    name VARCHAR NOT NULL 
);

"""

order_table = """
CREATE TABLE IF NOT EXISTS orders(
    order_id serial PRIMARY KEY, 
    user_id int NOT NULL ,
    name VARCHAR NOT NULL ,
    qty INT NOT NULL
    
    
);
"""
def create_tables():
    queries = [user_table,admin_table,meals_table,order_table]
    for i in queries:
        cur.execute(i)
        conn.commit()
        

def drop_tables():
    query1 = "DROP TABLE users"
    query2 = "DROP TABLE meals"
    query3 = "DROP TABLE orders"
    query4 = "DROP TABLE admin"
    queries = [query1,query2,query3,query4]
    for i in queries:
        cur.execute(i)
        conn.commit()
        



#tables = [user_table, meals_table, category_table, order_table ]
