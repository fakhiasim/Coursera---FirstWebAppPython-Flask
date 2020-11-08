#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField #input tyes as string and submit
#from wtforms.validators import DataRequired #Tovalidate input is not empty
#from wtforms.validators import *

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class  AddTaskForm(FlaskForm):
    
    title = StringField('Title : ', validators=[DataRequired()])
    submit = SubmitField('Submit')

#Althoug we have created this form it wont be present in the web page
# we need to import it in routes and include an instance of it.