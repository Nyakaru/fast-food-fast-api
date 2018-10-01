from ..database.connect import create_conn
from flask_bcrypt import Bcrypt
from psycopg2.extras import RealDictCursor

class UserModel:
    Admin = 2
    customer = 1
    
    def __init__(self, data={}):
        self.username = data.get('username')
        self.email = data.get('email')
        self.role = UserModel.customer
        self.enc = Bcrypt()
        self.password = self.enc.generate_password_hash(data.get('password')).decode('utf-8')
        self.db = create_conn()    

    def get_user_by_email(self):
        con, response = self.db, None
        cur = con.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute("select * from users WHERE email='{}'".format(self.email))
            response = cur.fetchall()
        except Exception as e:
            print(e)
        con.close()
        return response

    def save(self):
        data, conn = None, self.db
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            query = "INSERT INTO users (user_name, email, password, role) values(%s, %s, %s, %s)"
            cursor.execute(query, (self.username,self.email,self.password, self.role  ))
            conn.commit()
            data = cursor.fetchone()
            cursor.close()   
        except Exception as e:
            print(e)
        return data
       


    
