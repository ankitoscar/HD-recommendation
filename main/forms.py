from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, RadioField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField
from main.models import User

#so obviously imported Flaskform
#imported RecaptchaField from flask_wtf because it is somewhat different from ususal wtforms fields
#imported fields
#imported validators
#imported the Datefield from html5, this shows the drop down thing 


class signupform(FlaskForm):

    
    birthdate = StringField('Age', validators=[DataRequired()])

    recaptcha = RecaptchaField()

    #RecaptchaField() --> just enables the recaptcha thing at this place, recaptcha is a little different as it requires keys to be put in the main file, the keys we recieve from the recaptcha providing host.
                # I used GOOGLE recaptcha services

    

    radios = RadioField('Gender', default='3', choices= [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Confidential')])

    #RadioField --> basiaacally the choose from options
            #--> in our form helpers we have used these such that the first value in choices is the id and second is the label



    #basically a drop down seclection
    #acts as a pop up radio field thing but works with the form helper of regular things
    submit = SubmitField('Sign Up')
    
    #Genertaes a submit button which acts as post




