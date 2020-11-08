#4. Extending templates
from flask import Flask,render_template

#When we run a script there is special variable __name__ assigned a value __main__
#it is when you directly runnyng itusing python interpretor
#We create an instance of Flask
app = Flask(__name__)
#Till here the app is present but it does nont really do anthing special.
#In order to tell what page to show on browser we need to define routes.

@app.route('/')#this is a decorator tells python to return below funtion
@app.route('/index') #define multiple routes to same function
def index():
    return render_template('index.html',page_title = "Home")

#In addition to text we can also return html tags.
#Infact you can retun complete html pages
#to do so we need to import render_template and use it to return html file
#Another cool thing about templates is that you can pass arguments to funtion
#and use it inside the html file using {{ argument }}

@app.route('/about')
def about():
    return  render_template('about.html',page_title = "About")
#Heere we defined another page about but it is going to contain same so we create base template for it.and reuse it.


#Now we check if the app.py is exucuted from command line
if __name__ == '__main__':
    app.run(debug=True) #run the app in debug mode