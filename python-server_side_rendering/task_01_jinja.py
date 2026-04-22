from flask import Flask, render_template

'''Begins here'''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Запуск на порту 5000 с включенным дебагом для удобства разработки
    app.run(debug=True, port=5000)
