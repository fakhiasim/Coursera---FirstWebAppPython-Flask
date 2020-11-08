#Here this file is not aware about app
#lets imprt it from app3

from app4 import app,db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime
import forms


@app.route('/')#this is a decorator tells python to return below funtion
@app.route('/index') #define multiple routes to same function
def index():
    tasks = Task.query.all()
    return render_template('index.html',page_title = "Home")


@app.route('/add', methods=['GET','POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        #print ('Submitted title : ', form.title.data)``
        t = Task(title=form.title.data, date=datetime.utcnow())
         
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return  render_template('add.html',page_title = "About", form=form)
#Here we defined another page about but it is going to contain same so we create base template for it.and reuse it.
