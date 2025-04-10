from flask import Blueprint, render_template, request
from schedule.app import db
from schedule.blueprints.activities.models import Activity
from datetime import datetime

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    date_str = request.args.get('date')
    if date_str:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        selected_date = datetime.today().date()

    today_activities = db.session.query(Activity).filter(Activity.date == selected_date).all()
    return render_template('home/index.html', activities=today_activities, selected_date=selected_date)