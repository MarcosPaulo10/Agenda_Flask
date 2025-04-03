from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    
    app.config["SECRET_KEY"] = "570e517ee7haff3f2c5aa442088af43cdcbecf334c2b5370a24cd5a65d99106b"
    crsf = CSRFProtect(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
    
    db.init_app(app)
    
    # import and register all blueprints -------------------------i
    from schedule.blueprints.home.routes import home
    app.register_blueprint(home, url_prefix='/')
    
    from schedule.blueprints.activities.routes import activity
    app.register_blueprint(activity, url_prefix='/activities')
    
    from schedule.blueprints.tools.routes import tool
    app.register_blueprint(tool, url_prefix='/tool')
    # ------------------------------------------------------------f
    
    migrate = Migrate(app, db)

    return app