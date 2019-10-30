from flask import Flask, render_template
from flask_socketio import SocketIO
from game import Game
from time import monotonic

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey!1234'
io = SocketIO(app, async_mode='threading')

WORLD_SIZE = 512
engine_frequency = 4.0

the_game = Game(WORLD_SIZE)

@app.route('/')
def index():
    return render_template('index.html', world_size=WORLD_SIZE)


@io.on('connect')
def connect():
    print('Connect')


@io.on('disconnect')
def disconnect():
    print('Disconnect')

    
def update_task():
    t = monotonic()
    while True:
        # TODO: Figure out why the program hangs here if the
        # eventlet async_mode is used instead of threading
        io.sleep(1 / engine_frequency)
        now = monotonic()
        dt = now - t
        t = now
        
        the_game.update(dt)
        io.emit('update', the_game.serialize_state())
    
    
if __name__ == '__main__':
    task = io.start_background_task(update_task)
    io.run(app, debug=True)
