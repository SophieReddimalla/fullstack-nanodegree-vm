from flask import flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if _name_ == '_main_':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)