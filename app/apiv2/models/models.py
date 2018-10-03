import os
import psycopg2
from datetime import datetime
from werkzeug.security import generate_password_hash


def connection():
    
    try:
        connection = psycopg2.connect(
            database = os.getenv('DB'),
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD")
            
            )
        
        return connection

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
conn = connection()
print conn
cur = conn.cursor()

class User():
    def __init__(self,
                 username=None,
                 email=None,
                 password=None
                 ):
        
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
           

    def add(self):
        ''' Add users to user table'''
        cur.execute(
            ''' INSERT INTO users(username, email, password) VALUES(%s, %s,%s)''',
            (self.username, self.email, self.password))

        conn.commit()
        

    def get_user_by_username(self, username):
        ''' get user by username '''
        f = "SELECT * FROM users WHERE username='{}'".format(username)
        cur.execute(f)
                           

        user = cur.fetchone()

        conn.commit()
        

        if user:
            return self.objectify_user(user)
        return None



    def serialize(self):
        '''return an object as dictionary'''
        return dict(
            id=self.id,
            username=self.username,
            password=self.password,
            email=self.email
            
            )

    def objectify_user(self, data):
        ''' change a tuple user to an object '''
        self.id = data[0]
        self.username = data[1]
        self.password = data[2]
        self.email = data[3]
        
        

        return self  

class MealItem():
    def __init__(self, name=None, description=None, price=None):
        
        self.name = name
        self.description = description
        self.price = price

    def add(self):
        ''' Add food item to fooditems table'''
        cur.execute(
            ''' INSERT INTO meals(name, description, price) VALUES(%s, %s, %s)''',
            (self.name, self.description, self.price))

        conn.commit()

        

    def get_all_meals(self):
        '''  Get all food meals '''
        cur.execute(''' SELECT * FROM meals''')

        meals = cur.fetchall()

        conn.commit()
        

        if meals:
            return [self.objectify(meal) for meal in meals]
        return None

    def serialize(self):
        ''' Return object as dictionary '''
        return dict (
            id = self.id,
            name = self.name,
            description = self.description,
            price = self.price
        )

    def objectify(self, data):
        ''' map tuple to an object '''
        item = MealItem(name=data[1], description=data[2], price=data[3])
        item.id = data[0]
        self = item
        return self


        
class Order():
    def __init__(self,
                # id = None,
                 username=None,
                 title=None,
                 description = None,
                 price=None,
                 status="Pending"):
        
        self.username = username
        self.title = title
        self.description = description
        self.price = price
        self.status = status
        

    def add(self):
        ''' Add food order to database'''
        print(self.username)
        cur.execute(
            """ INSERT INTO orders(username, title, description, price, status) VALUES('%s','%s','%s','%s','%s')""" %
            (self.username, self.title, self.description, self.price,self.status))

        conn.commit()
        

    def get_by_id(self, order_id):
        '''fetch an order by id'''
        cur.execute(''' SELECT * FROM orders WHERE id=%s''',
                            (order_id, ))

        order = cur.fetchone()

        conn.commit()
        

        if order:
            return self.objectify(order)
        return None

    def get_all_orders(self):
        '''  Get all food orders '''
        cur.execute(''' SELECT * FROM orders''')

        orders = cur.fetchall()

        conn.commit()
        

        if orders:
            return [self.objectify(order) for order in orders]
        return None

    def delete(self, order_id):
        ''' Delete order '''
        cur.execute(''' DELETE FROM orders WHERE id=%s''',
                            (order_id, ))
        conn.commit()
        

    def serialize(self):
        ''' return object as a dictionary '''
        return dict (
            id = self.id,
            title = self.title,
            description = self.description,
            price = self.price,
            status = self.status,
            date = self.date
        )
    
    def objectify(self, data):
        ''' map tuple to an object '''
        order = Order(
            username=data[1],
            description=data[2],
            title=data[3],
            price=data[4],
            status=data[5])
        order.id = data[0]
        order.date = str(data[6])
        self = order
        return self
          