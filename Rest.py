from flask import Flask
from GameEngine import GameEngine
app = Flask(__name__)

engine = GameEngine()

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/firstplayer')
def first_player():
    return engine.first_player()

@app.route('/secondplayer')
def second_player():
    return engine.second_player()

if __name__ == '__main__':
    app.run()
