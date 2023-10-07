#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_creator = request.form.get('button_creator')

    if button_python == "SHOW PROJECT":
        return render_template('index.html', button_python=button_python)
    elif button_discord == "SHOW PROJECT":
        return render_template('index.html', button_discord=button_discord)
    elif button_html == "SHOW PROJECT":
        return render_template('index.html', button_html=button_html)
    elif button_creator == "SHOW PROJECT":
        return render_template('index.html', button_creator=button_creator)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)



