from flask import Flask
from flask import abort
from flask import redirect
from flask import make_response

app = Flask(__name__)

@app.route('/user/<name>')
def hello(name):#attention param name
    if name != 'zhang':
        abort(404) #
    return '<h1>hello %s</h1>' % name

@app.route('/')
def index():
        return redirect('http://www.baidu.com')

@app.route('/resp')
def resp():
    response = make_response('<h1>this document carries a cookie</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
