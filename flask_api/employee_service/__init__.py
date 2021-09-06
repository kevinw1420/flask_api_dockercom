# serveic class
from flask import Flask
from flask_api.config import config
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(config['default'])

@app.route("/test")
def index():
    return 'Test'
# serveic manager instance
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow()
Migrate(app,db)

from . import views