import psycopg2
import os 
from .create_tables import queries, to_drop
from flask import current_app

#create a connection
def create_conn():
    url = current_app.config.get('POSTGRES_DATABASE_URI')
    conn = psycopg2.connect(url)
    return conn

#Create Database tables for tests
def create_db(): 
    conn = create_conn()
    curr = conn.cursor()
    conn.autocommit = True
    for query in queries:
        curr.execute(query)

    curr.close()
    conn.commit()
    return conn


# drop table for tests
def drop_db():
    conn = create_conn()
    curr = conn.cursor()
    try: 
        for query in to_drop:
            curr.execute(query)

        curr.close()
        conn.commit()
    except:
        print("failed")