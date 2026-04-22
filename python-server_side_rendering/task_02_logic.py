import json
from flask import Flask, render_template

'''Begins here'''

app = Flask(__name__)

# Маршруты из предыдущих задач
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# НОВЫЙ МАРШРУТ: Динамический список товаров
@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Извлекаем список по ключу "items", если ключа нет — возвращаем пустой список
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не найден или поврежден, передаем пустой список
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
