# Flask-Web-App-with-MySQL-Database-Authentication-and-Notes-Feature

## A fully functional Example project written in Python showing how to create a Flask Web application that requests Database authentication and allows one to

### Introduction:
This is a simple Flask web application that allows users to sign up, log in, and write and save notes. The application uses MySQL for storing user details and notes. It incorporates Flask for web development, Werkzeug for password hashing, Flask-Login for user session management, and SQLAlchemy for database interaction.

### Prerequisites:
* Make sure you have Python and pip installed on your machine. You can use an IDE of your choice but I suggest Pycharm for this project
* Make sure you download XAMPP to connect to MySQL. https://www.apachefriends.org/download.html
* Open PHPMYADMIN using this url link on your browser http://localhost/phpmyadmin

### Install the required dependencies and libraries:
```pip install -r requirements.txt```

```pip install Flask Flask-Login Flask-SQLAlchemy mysql-connector-python```

### Create the MySQL database:
Your can create MYSQL database inside PHPMYADMIN

### Connecting to the database to perform CRUD functions:
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost/database_name'
- _Replace username, password, and database_name with your MySQL credentials._

### Run the Flask application on Pycharm:
Run python main.py
- Visit http://127.0.0.1:5000 in your web browser.

### Usage:
1. Open the web app and sign up for a new account.
2. Log in with your credentials.
3. Navigate to the homepage to write and save notes.

### Libraries Used
- Flask: A web framework for Python.
- Flask-Login: Provides user session management for Flask.
- Flask-SQLAlchemy: Adds SQLAlchemy support to Flask.
- Werkzeug: A WSGI utility library for Python.

### Additional Notes:
1. User passwords are hashed using Werkzeug for security.
2. SQLAlchemy is used to interact with the MySQL database.
3. User input is validated using Python validation processes.

#### Author

Gabriel Mokhele


Feel free to add any home page of your choice and implement backend python code to add functionality to its front end with additional features like CSS & JS static files etc.
