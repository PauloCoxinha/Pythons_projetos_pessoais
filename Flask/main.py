from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundolllllllllkkkkkkkkk'

@app.route('/canal')
def canal():
    return 'Olá você estaaaaa acessando a rota canal'

@app.route('/ola/<nome>')
def ola(nome):
    nome = escape(nome)
    return f"Olá {nome}"
if __name__ == '__main__':
    app.run(debug=True)