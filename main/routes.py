
from flask import  render_template, url_for, flash, redirect
from main import app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from main.forms import signupform
from main.models import User
from main import db
import random
#from flask_login import current_user



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title_given="Home")


@app.route("/result", methods=['GET', 'POST'])
def result():
    
    return render_template("result.html", title_given="Result")
    
    


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = signupform()
    if form.validate_on_submit():
                
        new_user = User(age = form.birthdate.data, gender = form.radios.data, date_account_created = datetime.now().date(), timestamp_first_active = datetime.timestamp(datetime.now()),  date_first_booking = datetime.now().date(), signup_method = 'direct', signup_flow = 'basic', language = 'en', affiliate_channel ='direct', affiliate_provider = random.choice(['direct','google','other','facebook','bing','craigslist']), first_affiliate_tracked = random.choice(['tracked', 'untracked']), signup_app = random.choice(['Web','Moweb']), first_device_type = random.choice(['Mac Desktop', 'Windows Desktop', 'iPhone', 'iPad','Other/Unknown']), first_browser = random.choice(['Chrome','Safari','Firefox','Mobile Safari','IE','Chrome Mobile','unknown']))
        db.session.add(new_user)
        db.session.commit()

        
        flash('The input is successfully recorded in our database', 'success')
        return redirect(url_for('result'))

    return render_template("signup.html", title_given="SignUp", form=form)


