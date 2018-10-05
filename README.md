# fast-food-fast-api


fast-food-fast-api is a backend for a fast food delivery service app for a restaurant.


### Branches
* master - main branch: all source after review and feedback.
* develop - all the features developed.
* challenge2 - contains all the features created with all the necessary pages to allow the application function .
* challenge3 - contains all the features created with all the necessary pages to allow the application function using a database.

### Prerequisites

What you need to get started:

- [Python 3](https://www.python.org/download/releases/3.0/)

- [virtualenv](https://virtualenv.pypa.io/en/stable/)

- [Pip](https://pip.pypa.io/en/stable/installing/)

- [PostgreSQL](https://www.postgresql.org/download/)

- [Flask](http://flask.pocoo.org/)

#### Technologies used
    - Python 3.6
    - Flask
    - Flask_RESTful
    - Travis CI
    - Func Tools
    - Psycopg2

### Installing

- #### *Make sure PostgreSQL server is installed and running, then create databases:*

    - Log in to postgres account 

        ``` 
        $ psql --user postgres 
        ```

    - Create main database 

        ``` 
        postgres=# CREATE DATABASE foodfast; 
        ```

    - Create test database 
    
        ``` 
        postgres=# create database fastfoodtest_db; 
        ```

- #### *Clone this repo :*

    ```
    $ git clone https://github.com/Nyakaru/fast-food-fast-api.git
    ```

- ####  *Move to project directory :*
    
    ``` 
    $ cd fast-food-fast-api 
    ```

- #### *Create your Virtual Environment :*
    
    ```
    $ python3.6 -m venv [environment-name]
    ```

- #### *Activate your virtual environment :*
    
    ```
    $ source [environment-name]/bin/activate 
    ```

- #### *Install project requirements :*
    
    ```
    $ pip install -r requirements.txt 
    ```

- #### *Set up database :*
    
    ```
    $ python3 foodfast.py  
    
    ``` 

- #### *Start the app :*
    
    ```
    $ flask run 
    ``` 

- *You can now access the API from:* 
    
    ```
    http://localhost:5000/api/v2
    ``` 
## Running the tests

- With Coverage Report: 
    
    ```
    $ pytest --with-coverage --cover-package=app/api/v2 --cover-html 
    ```

## Documentation

Documentation can be accessed on:

    https://documenter.getpostman.com/view/5294981/RWgnXL2o
### Hosting

### Api Documentation
https://documenter.getpostman.com/view/5294981/RWgjYMBB

## Endpoints

| URL                                                       | Methods | Description              | Requires Auth  |
|-----------------------------------------------------------|---------|--------------------------|----------------|
| `/api/v2`                                                 | GET     | The base URL             | FALSE          |
| `/api/v2/auth/signup`                                     | POST    | Register User            | FALSE          |
| `/api/v2/auth/login`                                      | POST    | Login User               | FALSE          |
| `/api/v2/meals`                                            | POST    | Creates Meal             | TRUE           |
| `/api/v2/meals`                                            | GET     | Gets all meals           | FALSE          |
| `/api/v2/users/orders`                                    | POST    | Creates an order         | TRUE           |
| `/api/v2/users/orders`                                    | GET     | Returns all users orders | TRUE           |
| `/api/v2/users/orders/<int:id>`                           | GET     | Returns one order        | TRUE           |
| `/api/v2/users/history`                                   | GET     | Gets user's order history| TRUE           |
| `/api/v2/users/orders/<int:id>`                           | PUT     | Updates order status     | TRUE           |
| `/api/v2/users/orders/<int:id>`                           | DELETE  | Deletes an order         | TRUE           |
| `/api/v2/meals/<int:id>`                                   | DELETE  | Deletes a meal item      | TRUE           |


### Author
Developed by:
.. Nyakaru Kinara
[![Build Status](https://travis-ci.org/Nyakaru/fast-food-fast-api.svg?branch=develop)](https://travis-ci.org/Nyakaru/fast-food-fast-api)
[![Coverage Status](https://coveralls.io/repos/github/Nyakaru/fast-food-fast-api/badge.svg?branch=challenge2)](https://coveralls.io/github/Nyakaru/fast-food-fast-api?branch=challenge2)














