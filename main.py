from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<img src="/static/Line.jpg" class="d-block mx-auto" alt="...">'

if __name__ == '__main__':
    app.run()