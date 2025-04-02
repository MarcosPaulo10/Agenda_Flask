from flask import Blueprint, render_template
from schedule.app import db
from schedule.blueprints.activities.models import Activity
from datetime import datetime

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    today_activities = db.session.query(Activity).filter(Activity.date == datetime.today().date()).all()
    return render_template('home/index.html', activities = today_activities)