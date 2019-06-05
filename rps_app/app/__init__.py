from flask import Flask

app = Flask(__name__)

from rps_app.app import views  # noqa
