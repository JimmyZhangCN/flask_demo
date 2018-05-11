from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def hello(name):#attention param name 
    return '<h1>hello %s</h1>' % name


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
