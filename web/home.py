from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
from motuus.movement.movement import Movement
from motuus.player import Player

# to run on gunicorn: gunicorn --worker-class eventlet -w 1 motuus.web.home:app -b 0.0.0.0:5000
# need to install gunicorn and eventlet
# otherwise use flask (python home.py)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('home.html')
    # return render_template('index.html')


@socketio.on('my event', namespace='/test')
def test_message(message):
    # print message['data']
    m = Movement(message['data'])
    if session.get('PLAYER') is None:
        session['PLAYER'] = Player()
    session['PLAYER'].play(m)
    emit('my response', {'data': message['data']})


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=False, host="0.0.0.0")
