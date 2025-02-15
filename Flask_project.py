from flask import Flask # импортирует класс Flask из модуля flask
from flask import render_template
app = Flask (__name__) # создаём инстанс класса


@app.route('/radiobuttons')
def show_radiobuttons():
    return render_template('radiobuttons.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
'''debug mode - автоматически перезагружает сервер при внесении изменений в код'''

