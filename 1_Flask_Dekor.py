# Открытие ссылки на сайт http://127.0.0.1:5000/

from flask import Flask #Подключение библиотеки

# Создаём переменную app в которую мы сохраняем экземпляр класса Flask с переменной __name__
app = Flask(__name__)

# Декоратор для прописывания маршрута, url адресов функциям. Одна функция работает с одной web страницей
@app.route("/") # Декоратор
def hello_world(): # функция
    return "Hello World!" # Возвращаем ответ на экран

# Проверяем работу приложения, запускаем его
if __name__ == "__main__":
    app.run()