from flask import render_template, request

from rps_app.app import app
from rps_app.app.forms import GameForm


@app.route('/', methods=['POST', 'GET'])
def home():
    form = GameForm(request.form)

    if form.is_submitted():
        move = form.move.data
        result = dict(
            move=move,
            opponent_move='paper',
            is_winner=True,
        )
        return render_template('home.html', form=form, result=result)

    return render_template('home.html', form=form)
