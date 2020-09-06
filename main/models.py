
from main import db
from main import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    date_account_created = db.Column(db.String(), unique= False)

    timestamp_first_active = db.Column(db.String(), unique= False)

    date_first_booking = db.Column(db.String(), unique= False)

    age = db.Column(db.String(120), unique=False, nullable=False)

    gender = db.Column(db.String(120), unique=False, nullable=False)

    signup_method = db.Column(db.String())

    signup_flow = db.Column(db.String())

    language = db.Column(db.String())

    affiliate_channel = db.Column(db.String())

    affiliate_provider = db.Column(db.String())

    first_affiliate_tracked = db.Column(db.String())

    signup_app = db.Column(db.String())

    first_device_type =  db.Column(db.String())

    first_browser =  db.Column(db.String())

    
