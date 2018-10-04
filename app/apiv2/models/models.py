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

    def get_by_name(self, name):
        '''fetch an item by name'''

        g ="SELECT * FROM meals WHERE name='{}'".format(name)
        cur.execute(g)

        meal = cur.fetchone()

        conn.commit()
        

        if meal:
            return self.objectify(meal)
        return None

        

    def get_all_meals(self):
        '''  Get all food meals '''
        f = "SELECT * FROM meals"
        cur.execute(f)
                           

        meals = cur.fetchall()

        return meals
        

        #if meals:
            #return meals
            #for meal in meals:
                #return self.objectify_meal(meal)
        #return {'message':"Meals not found/"}


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
        cur.execute(
            ''' INSERT INTO orders(name, qty) VALUES(%s,%s)''',
            (self.name, self.qty))

        conn.commit()
    

    def get_by_id(self, order_id):
        '''fetch an order by id'''
        j = "SELECT * FROM orders WHERE order_id='{}'".format(order_id)
        cur.execute(j)                   

        order = cur.fetchone()

        conn.commit()
        

        if order:
            return self.objectify(order)
        return None

    def get_by_username(self, username):
        '''fetch orders by username'''
        v = "SELECT * FROM users WHERE username='{}'".format(username)
        cur.execute(v)
        orders = cur.fetchall()
        #print("\n\n\n####{}\n\n".format(orders))
        conn.commit()
      
        if orders:
            return [self.objectify(order) for order in orders]
        return None

        

    def get_all_orders(self):
        '''  Get all food orders '''
        cur.execute(''' SELECT * FROM orders''')

        orders = cur.fetchall()

        conn.commit()
        

        if orders:
            return [self.objectify(order) for order in orders]
        return None

    def get_order_history(self, username):
        ''' fetch all orders of a particular user'''
        d = "SELECT * FROM users WHERE username='{}'".format(username)
        
        cur.execute(d)
        
        orders = cur.fetchall()
        #print("\n\n\n####{}\n\n".format(orders))
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
            name = self.name,
            qty = self.qty
        )
    
    def objectify(self, data):
        ''' map tuple to an object '''
        order = Order(
            name=data[1],
            qty=data[2],
            )
        order.id = data[0]
        self = order
        return self
          






