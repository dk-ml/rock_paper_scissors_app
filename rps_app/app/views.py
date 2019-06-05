from rps_app.app import app


@app.route('/')
def home():
    return 'Welcome to rock, paper, scissors!'
