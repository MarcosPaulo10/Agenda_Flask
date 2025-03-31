from flask import Blueprint, render_template
from schedule.app import db

tool = Blueprint('tool', __name__, template_folder='templates')

@tool.route('/')
def index():
    return render_template('tools/index.html')