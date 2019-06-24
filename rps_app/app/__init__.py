import os

from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
bootstrap = Bootstrap(app)

from rps_app.app import views  # noqa
