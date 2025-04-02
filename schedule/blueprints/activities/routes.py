from flask import Blueprint, render_template, request, redirect, url_for
from schedule.app import db
from datetime import datetime

from schedule.blueprints.activities.models import Activity, Category

activity = Blueprint('activity', __name__, template_folder='templates')


@activity.route('/', methods=['POST', 'GET'])
def index_activity():
    if request.method == 'GET':
        activities = Activity.query.all()
        return render_template('activities/index_activity.html', activities=activities)
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        done = request.form.get("done") == "on"
        category_id = request.form.get('category_id')
        
        formated_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        formated_start_time = datetime.strptime(start_time, "%H:%M").time() if start_time else None
        formated_end_time = datetime.strptime(end_time, "%H:%M").time() if end_time else None
        
        activity = Activity(
            name = name, 
            description = description, 
            date = formated_date, 
            start_time = formated_start_time, 
            end_time = formated_end_time, 
            done = done, 
            category = category_id
        )
        
        db.session.add(activity)
        db.session.commit()
        
        return redirect(url_for('activity.index_activity'))
    
@activity.route('/category', methods=['POST', 'GET'])
def index_category():
    if request.method == 'GET':
        categories = Category.query.all()
        return render_template('activities/index_category.html', categories=categories)
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        category_father = request.form.get('category_id')
        
        category = Category(name=name, description=description, category_father=category_father)
        db.session.add(category)
        db.session.commit()
        
        return redirect(url_for('activity.index_category'))
    
@activity.route('/teste')
def teste():
    return render_template('activities/teste.html')

@activity.route('/info_activity/<int:id>')
def info_activity(id):
    activity = Activity.query.get(id)
    return render_template('activities/activity_info.html', activity=activity)

@activity.route('/info_category/<int:id>')
def info_category(id):
    category = Category.query.get(id)
    return render_template('activities/category_info.html', category=category)