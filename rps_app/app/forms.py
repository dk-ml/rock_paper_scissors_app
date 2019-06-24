from flask_wtf import FlaskForm
from wtforms import StringField


class GameForm(FlaskForm):
    move = StringField(label='Move')
