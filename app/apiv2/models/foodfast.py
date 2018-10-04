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

category_table = """
CREATE TABLE IF NOT EXISTS category(
    category_id serial PRIMARY KEY,
    category_name VARCHAR NOT NULL
);
"""

order_table = """
CREATE TABLE IF NOT EXISTS orders(
    order_id serial PRIMARY KEY, 
    name VARCHAR NOT NULL ,
    qty INT NOT NULL
    
    
);
"""
def create_tables():
    cur.execute(user_table)
    cur.execute(meals_table)
    cur.execute(category_table)
    cur.execute(order_table)
    cur.execute(admin_table)
    conn.commit()
    cur.close()
    conn.close()


if __name__=='__main__':
    create_tables()

#tables = [user_table, meals_table, category_table, order_table ]