import os
import psycopg2
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

class Admin():
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
            ''' INSERT INTO admin(username, email, password) VALUES(%s, %s,%s)''',
            (self.username, self.email, self.password))

        conn.commit()

    def get_admin_by_username(self, username):
        ''' get admin by username '''
        f = "SELECT * FROM admin WHERE username='{}'".format(username)
        cur.execute(f)
                           

        admin = cur.fetchone()

        conn.commit()
        

        if admin:
            return self.objectify_admin(admin)
        return None




    def serialize(self):
        '''return an object as dictionary'''
        return dict(
            id=self.id,
            username=self.username,
            password=self.password,
            email=self.email
            
            )

    def objectify_admin(self, data):
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

    def get_by_name(self, name):
        '''fetch an item by name'''

        g ="SELECT * FROM meals WHERE name='{}'".format(name)
        cur.execute(g)

        meal = cur.fetchone()

        conn.commit()
        

        if meal:
            return {
            "mealname":meal[1]
            }
        return None

        

    def get_all_meals(self):
        '''  Get all food meals '''
        f = "SELECT * FROM meals"
        cur.execute(f)
                           

        meals = cur.fetchall()
        conn.commit()
        if meals:
            return [self.objectify_meal(meal) for meal in meals]
        return None

        return (meals)
    

    def serialize(self):
        ''' Return object as dictionary '''
        return dict (
            id = self.id,
            name = self.name,
            description = self.description,
            price = self.price
        )

    def objectify_meal(self, data):
        ''' map tuple to an object '''
        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.price = data[3]

        return self


        
class Order():
    def __init__(self,
                # id = None,
                 name=None,
                 qty=None,
                 ):
        
        self.name = name
        self.qty = qty
        
        
        

    def add(self):
        ''' Add food order to database'''
        #print(self.username)
        sql = "SELECT * from meals where name = %s;"
        cur.execute(sql,([self.name]))
        available = cur.fetchall()
        if available:
            cur.execute(
                ''' INSERT INTO orders(name, qty) VALUES(%s,%s)''',
                (self.name, self.qty))

            conn.commit()
            return True
        return False
    

    def get_all_orders(self):
        '''  Get all food orders '''
        cur.execute(''' SELECT * FROM orders''')

        orders = cur.fetchall()

        conn.commit()
        

        if orders:
            return [self.objectify(order) for order in orders]
        return None

    def get_order_by_id(self,id):
        '''  Get all food orders '''
        f = "SELECT * FROM orders WHERE id='{}'".format(id)
        cur.execute(f)
                           

        order = cur.fetchone()

        conn.commit()
        

        if order:
            return {"name":order[1]}
        return None
        

    def serialize(self):
        ''' return object as a dictionary '''
        return dict (
            
            name = self.name,
            qty = self.qty
        )
    
    def objectify_order(self, data):
        ''' map tuple to an object '''
        order = Order(
            name=data[0],
            qty=data[1],
            )
        #order.id = data[0]
        self = order
        return self
          






