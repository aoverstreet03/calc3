from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello workd"

@app.route('/alexis')
def alexis():
    return "hello alexis"

if __name__ == '__main__':
    app.run(debug=True)
