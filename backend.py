from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'


app.run(debug=True)
