from flask import Flask
from servo_handler import ServoHandler

app = Flask(__name__)
sh =  ServoHandler()


@app.route('/api/<int:range>')
def hello_world(range):
    sh.move(range)
    return f'your values is: {range}'


if __name__ == '__main__':
    app.run()
