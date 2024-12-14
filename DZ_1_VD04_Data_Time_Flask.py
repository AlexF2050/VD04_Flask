from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def date_time():
    now = datetime.now()
    return f'<div style="text-align: center; color: white; background-color: green; display: flex; justify-content: center; align-items: center; height: 100vh;">Текущая дата и время: {now.strftime("%Y-%m-%d %H:%M:%S")}</div>'

if __name__ == '__main__':
    app.run()




