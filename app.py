from flask import Flask

#When we run a script there is special variable __name__ assigned a value __main__
#it is when you directly runnyng itusing python interpretor
#We create an instance of Flask
app = Flask(__name__)
#Till here the app is present but it does nont really do anthing special.
#In order to tell what page to show on browser we need to define routes.

@app.route('/')#this is a decorator tells python to return below funtion
@app.route('/index') #define multiple routes to same function
def index():
    return 'Hello World!'



#Now we check if the app.py is exucuted from command line
if __name__ == '__main__':
    app.run(debug=True) #run the app in debug mode