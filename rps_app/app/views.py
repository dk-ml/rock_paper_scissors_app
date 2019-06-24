from flask import render_template, request
from rps.game import Game, Move
from rps.player import AIPlayer, ForcedPlayer

from rps_app.app import app
from rps_app.app.forms import GameForm

MOVES = {'ROCK': Move.ROCK, 'SCISSORS': Move.SCISSORS, 'PAPER': Move.PAPER}

human_player = ForcedPlayer()
game = Game(player1=human_player, player2=AIPlayer())


@app.route('/', methods=['POST', 'GET'])
def home():
    form = GameForm(request.form)

    if form.is_submitted():
        move = form.move.data
        human_player.next_move = MOVES[move.upper()]
        game.play_round()
        result = dict(
            move=game.history[-1][0],
            opponent_move=game.history[-1][1],
            is_winner=game.winners[-1],
        )
        return render_template('home.html', form=form, result=result)

    return render_template('home.html', form=form)
