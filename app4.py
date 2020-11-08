#4. SQL Alchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

#TO tell this file about routes
from routes import *

#Now we check if the app.py is exucuted from command line
if __name__ == '__main__':
    app.run(debug=True) #run the app in debug mode