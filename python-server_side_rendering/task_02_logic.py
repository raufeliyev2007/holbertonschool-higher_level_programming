import json
from flask import Flask, render_template

'''Begins here'''

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    # Важно: имя шаблона должно совпадать с файлом в папке templates
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
