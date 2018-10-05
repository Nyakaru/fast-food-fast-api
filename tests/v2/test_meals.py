import json

from flask import request

def test_table_items(create_client):
    create_client.post('/api/v2/meals',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"name":"chai","description":"tasty","price":"50"}))
    create_client.post('/api/v2/meals',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"name":"chai","description":"tasty","price":"50"}))
    response = create_client.get("/api/v2/meals")
    assert response.status_code == 404
def test_order_items(create_client):
	response = create_client.get("/api/v2/orders")
	assert response.status_code == 200
def test_one_order_items(create_client):
    create_client.post('/api/v2/orders', headers = {"Content-Type":'application/json'}, data = json.dumps({"name":"ugali", "qty":1}))
    response = create_client.get("/api/v2/orders")
    assert response.status_code == 200

def test_user_already_exists(create_client):
    response = create_client.post('/api/v2/auth/signup',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimani", "email":"martin@gmail.com","password":"password"}))
    response = create_client.post('/api/v2/auth/signup',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimani", "email":"martin@gmail.com","password":"password"}))
    assert response.status_code == 409

def test_signup_pass(create_client): #User sign up pass
    '''Test for user sign up'''
    response = create_client.post('/api/v2/auth/signup',
    	headers = {"Content-Type":'application/json'} , 
    	data =json.dumps({"username":"kimothp", "email":"martin@gmail.com","password":"password"}))
    
    assert response.status_code == 201
def test_login_pass(create_client): 
    '''Test for user login'''
    create_client.post('/api/v2/auth/signup',
    	headers = {"Content-Type":'application/json'} , 
    	data =json.dumps({"username":"kimani", "email":"martin@gmail.com","password":"password"}))
    response2 =create_client.post('/api/v2/auth/login',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimani", "password":"password"}))
    
    assert response2.status_code == 200
def test__order_not_exist(create_client):
	response = create_client.get("/api/v2/orders/100")
	assert response.status_code == 404
def test_meal_created(create_client):
	response = create_client.post('/api/v2/meals',
    	headers = {"Content-Type":'application/json'} , 
    	data =json.dumps({"name":"chai","description":"tasty","price":"50"}))
	assert response.status_code == 200
def test_meal_exists(create_client):
    create_client.post('/api/v2/meals',
    	headers = {"Content-Type":'application/json'} , 
    	data =json.dumps({"name":"ugali","description":"tasty","price":"50"}))
    create_client.post('/api/v2/meals',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"name":"ugali","description":"tasty","price":"50"}))
    response = create_client.get('/api/v2/meals')
    assert response.status_code == 404

def test_signadmin_pass(create_client): 
    '''Test for admin sign up'''
    response = create_client.post('/api/v2/signadmin',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimothp", "email":"martin@gmail.com","password":"password"}))

def test_loginadmin_pass(create_client): 
    '''Test for user sign up'''
    create_client.post('/api/v2/signadmin',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimani", "email":"martin@gmail.com","password":"password"}))
    response2 =create_client.post('/api/v2/loginadmin',
        headers = {"Content-Type":'application/json'} , 
        data =json.dumps({"username":"kimani", "password":"password"}))
    