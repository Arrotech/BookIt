[![Build Status](https://www.travis-ci.org/Arrotech/BookIt.svg?branch=develop)](https://www.travis-ci.org/Arrotech/BookIt) [![Coverage Status](https://coveralls.io/repos/github/Arrotech/BookIt/badge.svg?branch=develop)](https://coveralls.io/github/Arrotech/BookIt?branch=develop) [![codecov](https://codecov.io/gh/Arrotech/BookIt/branch/develop/graph/badge.svg)](https://codecov.io/gh/Arrotech/BookIt) [![Maintainability](https://api.codeclimate.com/v1/badges/a41605e60da75c12a1f6/maintainability)](https://codeclimate.com/github/Arrotech/BookIt/maintainability)


**BOOK IT**


**Product Overview**

Domestic tourism is fast on the rise. With a growing middle class with more disposable income, more
Kenyans are traveling within the country, visiting parks and staying in luxury hotels and lodges.
This application is meant to allow tourists able to book trips, hotels and lodges in advance.

Below are the Endpoints for the application.

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| /api/v1/auth/register | Create user| POST |
| /api/v1/auth/login | Login to account |GET|
| /api/v1/auth/refresh | Get access token | POST |
| /api/v1/auth/protected | Get logged in user email | GET |
| /api/v1/auth/users | Get all Users | GET |
| /api/v1/auth/users/username | Get a specific user | GET |
| /api/v1/auth/users/username | Make admin | PUT |
| /api/v1/hotels |  Add a hotel | POST |
| /api/v1/hotels | Get all hotels | GET |
| /api/v1/hotels/name | Get a specific hotel by name | GET |
| /api/v1/lodges |  Book a lodge | POST |
| /api/v1/lodges | Get all lodges | GET |
| /api/v1/lodges/booked_by | Get a specific lodge | GET |
| /api/v1/lodges/cancel/lodge_id | Cancel specific lodge | PUT |
| /api/v1/lodges/complete/lodge_id | Complete specific lodging | PUT |
| /api/v1/lodges/activate/lodge_id | Activate a specific lodging | PUT |
| /api/v1/trips |  Book a trip | POST |
| /api/v1/trips | Get all trips | GET |
| /api/v1/trips/booked_by | Get specific trip | GET |
| /api/v1/trips/cancel/trip_id | Cancel specific trip | PUT |
| /api/v1/trips/complete/trip_id | Complete specific trip | PUT |
| /api/v1/trips/in-progress/trip_id | Mark progress of a specific trip | PUT |


**TOOLS TO BE USED IN THE DEVELOPMENT**

1. Server-Side Framework: [Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library: [Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide: [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework: [PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Framework: [Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)


**REQUIREMENTS**

This are the basic project requirements. Make sure to install the before attempting to run the project.

	1. Python: [Install Python3](https://realpython.com/installing-python/)
	2. Postgres: [Install Postgres](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
	3. Git: [Install Git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04)
	4. Node: [Install Node](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04)
	5. Postman: [Install Postman](https://linuxize.com/post/how-to-install-postman-on-ubuntu-18-04/)

The others can be downloaded and install from the requirements file. The installation process is outlined in the section `How to run the application`.


**HOW TO RUN THE APPLICATION**

Note that this project is meant for linux.

 1. Make a new directory on your computer and name it `bookit` or give it any name of your choice.
 2. Navigate to the directory you have created and open it in the terminal.
 3. On the terminal type `git clone` and add this link <code>[repo](https://github.com/Arrotech/BookIt/)</code> and the press `enter` to clone the remote repository to your local repository i.e `git clone 'link'`. Add the link without the quotation.
 4. Navigate to the directory that has been cloned to your machine and open it in a terminal.
 5. Create virtual environment by typing this in the terminal `virtualenv -p python3 venv`.
 6. Run `pip install -r requirements.txt` on the terminal to install the dependencies.
 7. Then type on the terminal `source .env` to activate the environment and also to export all the environment variables.
 8. Then type on the terminal `flask run` to start and run the server.
 9. To run the HTML pages, make sure you have node already installed in your machine. Click [Here](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04) and follow the process to install node.
 10. Open another terminal and make sure the environment is activate. If not type `source .env` to activate it.
 11. The type `live-server` to run the pages locally.
 12. You can now interact with the project.


 **HOW TO RUN TESTS**

 1. Open a new terminal and then activate the environment.
 2. Type `pytest --cov=app --cov-report=term-missing` and hit `enter`. This will run all tests and then give you a Coverage with details.


 **OTHER IMPORTANT LINKS**

 1. Heroku deployment of the application: [Heroku](https://bookit-api-app.herokuapp.com/)
 2. Test coverage with coveralls: [Coveralls](https://coveralls.io/github/Arrotech/BookIt)


**AUTHOR**

     Harun Gachanja Gitundu, Software Engineer.
