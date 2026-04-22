import json
import csv
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
            # Преобразуем id в int для корректного сравнения
            row['id'] = int(row['id'])
            # Преобразуем price в float для красоты
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # 1. Проверка источника
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Чтение данных
    try:
        if source == 'json':
            data = read_json('products.json')
        else:
            data = read_csv('products.csv')
    except Exception as e:
        return render_template('product_display.html', error=f"File error: {e}")

    # 3. Фильтрация по ID
    if product_id:
        filtered_data = [p for p in data if p.get('id') == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
