from ..db.conn import create_conn
from psycopg2.extras import RealDictCursor
import json

class MenuModel:
    def __init__(self, data={}):
        self.menu_name = data.get('menu_name')
        self.menu_id = data.get('menu_id')
        self.table = data.get('table_name')
        self.db = create_conn()

    def get_by_id(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from menus WHERE menu_id='{}'".format(self.menu_id))
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response

    def get_by_name(self):
        con, response = self.db, None
        cur = con.cursor()
        try:
            
            cur.execute("select * from menus WHERE menu_name='{}'".format(self.menu_name))
            response = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return response

    def update_name(self):
        con= self.db
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("UPDATE menus SET menu_name='{}' WHERE menu_id='{}'".format(self.menu_name,self.menu_id))
            con.commit()
        except Exception as e:
            print(e)
        con.close()
        


    def get_all(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from {}".format(self.table))
            response = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return response

    def delete(self):
        con= self.db
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("delete from menus where menu_id='{}'".format(self.menu_id))
        except Exception as e:
            print(e)
        con.close()

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = "insert into menus (menu_name) values('{}')".format(self.menu_name)
            cursor.execute(query)
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except Exception as e:
            print(e)
        return data
            
    def is_json(self,data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True