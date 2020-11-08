#Here this file is not aware about app
#lets imprt it from app3

from app3 import app
from flask import render_template

import forms

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
    form = forms.AddTaskForm()
    return  render_template('about.html',page_title = "About", form=form)
#Here we defined another page about but it is going to contain same so we create base template for it.and reuse it.
