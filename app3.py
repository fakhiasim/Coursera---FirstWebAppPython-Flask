#4. Refactoring and forms -
#Mainly we would not store all the code in one file 
#so we will define all the routs in a different routes.py file
from flask import Flask

#When we run a script there is special variable __name__ assigned a value __main__
#it is when you directly runnyng itusing python interpretor
#We create an instance of Flask
app = Flask(__name__)
#Till here the app is present but it does nont really do anthing special.
#In order to tell what page to show on browser we need to define routes.

#Define Secret key to form submission
app.config['SECRET_KEY'] = 'secret-key'

#TO tell this file about routes
from routes import *

#Now we check if the app.py is exucuted from command line
if __name__ == '__main__':
    app.run(debug=True) #run the app in debug mode