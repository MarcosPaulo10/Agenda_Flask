from flask import Blueprint, render_template
from schedule.app import db

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    return render_template('home/index.html')