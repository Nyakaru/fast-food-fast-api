from ..db.conn import create_conn
from psycopg2.extras import RealDictCursor


class MealModel:
    def __init__(self, data={}):
        self.meal_name = data.get('meal_name')
        self.meal_id = data.get('meal_id')
        self.price = data.get('price')
        self.table = data.get('table_name')
        self.db = create_conn()
      

    def get_by_id(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from meals WHERE meal_id='{}'".format(self.meal_id))
            response = cur.fetchone()
        except Exception as e:
            print(e)
        con.close()
        return response

    def get_by_name(self):
        con, response = self.db, None
        cur = con.cursor()
        try:
            
            cur.execute("select * from meals WHERE meal_name='{}'".format(self.meal_name))
            response = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return response

    def update_name(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("UPDATE meals SET meal_name='{}' WHERE meal_id='{}'".format(self.meal_name,self.meal_id))
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
            cur.execute("delete from meals where meal_id='{}'".format(self.meal_id))
            con.commit()
        except Exception as e:
            print(e)
        con.close()

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = "insert into meals (meal_name, price) values('{}','{}')".format(self.meal_name, self.price)
            cursor.execute(query)
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except Exception as e:
            print(e)
        return data
            