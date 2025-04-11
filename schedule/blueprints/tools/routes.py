from flask import Blueprint, render_template, request, redirect, url_for
from schedule.app import db
from .models import Idea

tool = Blueprint('tool', __name__, template_folder='templates')

@tool.route('/')
def index():
    return render_template('tools/index.html')

@tool.route('/pomodoro')
def pomodoro():
    return render_template('tools/pomodoro.html')

@tool.route('/ideas')
def ideas():
    ideas = Idea.query.all()
    return render_template('tools/ideas.html', ideas=ideas)

@tool.route('/ideas/new_idea', methods=['POST', 'GET'])
def new_idea():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_idea = Idea(title=title, description=description)
        db.session.add(new_idea)
        db.session.commit()
        return redirect(url_for('tool.ideas'))
    return render_template('tools/new_idea.html')
        