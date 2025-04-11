from flask import Blueprint, render_template, request, redirect, url_for
from schedule.app import db
from datetime import datetime

from .models import Activity, Category

activity = Blueprint('activity', __name__, template_folder='templates')


@activity.route('/', methods=['POST', 'GET'])
def index_activity():
    if request.method == 'GET':
        activities = Activity.query.all()
        categories = Category.query.all()
        return render_template('activities/index_activity.html', activities=activities, categories=categories)
    
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
    
@activity.route('/done/<int:id>', methods=['POST'])
def done_activity(id):
    activity = Activity.query.get(id)
    activity.done = not activity.done
    db.session.commit()
    
    return redirect(url_for('home.index'))

@activity.route('/delete/<int:id>', methods=['POST'])
def delete_activity(id):
    activity = Activity.query.get(id)
    db.session.delete(activity)
    db.session.commit()
    
    return redirect(url_for('home.index'))

@activity.route('/edit_activity/<int:id>', methods=['POST', 'GET'])
def edit_activity(id):
    activity = Activity.query.get(id)
    categories = Category.query.all()
    
    if request.method == 'GET':
        return render_template('activities/edit_activity.html', activity=activity, categories=categories)
    
    if request.method == 'POST':
        activity.name = request.form.get('name')
        activity.description = request.form.get('description')
        
        date = request.form.get('date')
        formated_date = datetime.strptime(date, "%Y-%m-%d").date()
        activity.date = formated_date
        
        start_time = request.form.get('start_time')
        formated_start_time = datetime.strptime(start_time, "%H:%M").time() if start_time else None
        activity.start_time = formated_start_time
        
        end_time = request.form.get('end_time')
        formated_end_time = datetime.strptime(end_time, "%H:%M").time() if end_time else None
        activity.end_time = formated_end_time
        
        activity.done = request.form.get("done") == "on"
        activity.category = request.form.get('category_id')
        
        db.session.commit()
        
        return redirect(url_for('activity.activity_info', id=id))
    
@activity.route('/activity/<int:id>')
def activity_info(id):
    activity = Activity.query.get(id)
    categories = Category.query.all()
    return render_template('activities/activity_info.html', activity=activity, categories=categories)
    
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

@activity.route('/info_activity/<int:id>')
def info_activity(id):
    activity = Activity.query.get(id)
    return render_template('activities/activity_info.html', activity=activity)

@activity.route('/info_category/<int:id>')
def info_category(id):
    category = Category.query.get(id)
    return render_template('activities/category_info.html', category=category)