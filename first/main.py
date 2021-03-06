from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjhyutrtyrt6565hgft5564yrhfg6hfg6h7f'


menu = [{"name": "Главная", "url": "/"},
        {"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def index():
    # print( url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    # print(url_for('about'))
    return render_template('about.html', title='о сайте', menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')
        # print(request.form['username'])
    return render_template('contact.html', title="Обратная связь", menu = menu)


if __name__ == "__main__":
    app.run(debug=True)
