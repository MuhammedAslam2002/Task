from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello, World! hi aslam'
=======
    return 'Hello, World! hi guys'
>>>>>>> 230650601109e1465c70cf8c74628d516828b41e

if __name__ == '__main__':
    app.run(debug=True)
