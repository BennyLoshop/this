from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world(): # putapplication's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
