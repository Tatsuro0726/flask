from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form


app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xc9\x1b\xd2\xb1\x9d\xfd\x19T\xb5\xf0\xda$\x80\x02\xabB'

class UserForm(Form):
    name = StringField('名前')
    age = IntegerField('年齢')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = age = ''
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            age = form.age.data
            form.name.data = ''
            form.age.data = ''
        else:
            print('入力内容に誤りがあります。')
    
    return render_template('index.html', form=form, name = name, age=age)

if __name__ == '__main__':
    app.run(debug=True)