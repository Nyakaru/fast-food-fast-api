"""
Creating Data Tables
"""

dt1 = """ CREATE TABLE IF NOT EXISTS users(
    user_id serial PRIMARY KEY NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role INTEGER DEFAULT NULL,
    token VARCHAR(255) DEFAULT NULL,
    created_at timestamp with time zone DEFAULT now()
);"""

dt2 =""" CREATE TABLE IF NOT EXISTS meals(
    meal_id serial PRIMARY KEY NOT NULL,
    meal_name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now()
);"""

dt3 = """ CREATE TABLE IF NOT EXISTS menus(
    menu_id serial PRIMARY KEY NOT NULL,
    menu_name VARCHAR(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
);""" 



dt5 = """ CREATE TABLE IF NOT EXISTS orders(
    order_id serial PRIMARY KEY NOT NULL,
    meal_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    status INTEGER NOT NULL,
    total INTEGER NOT NUll,
    created_at timestamp with time zone DEFAULT now(),
    FOREIGN KEY (meal_id) REFERENCES meals (meal_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE ON DELETE CASCADE );
"""


drop_dt1 = """ DROP TABLE IF EXISTS users CASCADE

"""
drop_dt2 = """ DROP TABLE IF EXISTS meals CASCADE

"""
drop_dt3 = """ DROP TABLE IF EXISTS orders CASCADE

"""
drop_dt4 = """ DROP TABLE IF EXISTS menus CASCADE

"""
drop_dt5 = """ DROP TABLE IF EXISTS menuitems CASCADE

"""


to_drop = [drop_dt1, drop_dt2, drop_dt3, drop_dt4, drop_dt5]

queries = [dt1, dt2, dt5]