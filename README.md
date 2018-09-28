# fast-food-fast-api


fast-food-fast-api is a backend for a fast food delivery service app for a restaurant.


### Branches
* master - main branch: all source after review and feedback.
* develop - all the features developed.
* challenge2 - contains all the features created with all the necessary pages to allow the application function .

### Running and testing app
## Running:
```
$ virtualenv venv
$ cd venv
$ git clone https://github.com/Nyakaru/fast-food-fast-api.git
$ source venv/bin/activate
$ cd fast-food-fast-api
$ export APP_SETTINGS=development
$ python run.py
```
## Testing
Follow the above process then;
```
$ pytest -v
```
### Hosting
https://nyakaru-fast-food-fast.herokuapp.com/api/v1/orders

### Api Documentation
https://documenter.getpostman.com/view/5294981/RWgjYMBB

### Author
Developed by:
.. Nyakaru Kinara
[![Build Status](https://travis-ci.org/Nyakaru/fast-food-fast-api.svg?branch=develop)](https://travis-ci.org/Nyakaru/fast-food-fast-api)
[![Coverage Status](https://coveralls.io/repos/github/Nyakaru/fast-food-fast-api/badge.svg?branch=challenge2)](https://coveralls.io/github/Nyakaru/fast-food-fast-api?branch=challenge2)
