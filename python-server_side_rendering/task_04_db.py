import json
import csv
import sqlite3
from flask import Flask, render_template, request

'''Begins here'''

app = Flask(__name__)

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Row_factory позволяет получать данные в виде словарей, а не кортежей
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        # Превращаем объекты sqlite3.Row в обычные словари для шаблона
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        raise e # Пробрасываем ошибку выше для обработки в маршруте
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Валидация источника
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Получение данных из выбранного источника
    try:
        if source == 'json':
            data = read_json('products.json')
        elif source == 'csv':
            data = read_csv('products.csv')
        elif source == 'sql':
            data = read_sql()
    except Exception as e:
        return render_template('product_display.html', error=f"Database or File error: {e}")

    # 3. Фильтрация по ID (если указан)
    if product_id:
        filtered_data = [p for p in data if p.get('id') == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
