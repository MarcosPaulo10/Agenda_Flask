from schedule.app import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    category_father = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __repr__(self):
        return f'<Category {self.name}>'


class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    done = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Activity: {self.name} - {self.date}>'
    
class RecurringActivity(db.Model):
    __tablename__ = 'recurring_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    day_of_week = db.Column(db.Integer)
    day_of_month = db.Column(db.Integer)
    day_of_year = db.Column(db.Date)
    
    def __repr__(self):
        return f'<RecurringActivity: {self.name} - {self.start_date}>'
    