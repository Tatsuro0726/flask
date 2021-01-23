from flask import (
    Flask, render_template, request, session, redirect, url_for
)
from wtforms import Form
from wtforms import (
    StringField, IntegerField, BooleanField, DateField, PasswordField,
    RadioField, SelectField, TextAreaField, SubmitField
)
from wtforms.widgets import TextArea

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xc7\x06\xfb4sq\xa9\xa6\xa7\xc0\xcd\rX\xb5PL'

class UserForm(Form):
    name = StringField('名前:',widget=TextArea(), default='Flask太郎')
    age = IntegerField('年齢:')
    password = PasswordField('パスワード:')
    birthday = DateField('誕生日:', format='%Y/%m/%d', render_kw={"placeholder": "yyyy/mm/dd"})
    gender = RadioField('性別:', choices=[('man', '男性'), ('woman', '女性')], default='man')
    major = SelectField('専攻', choices=[('bungaku', '文学部'), ('hougaku', '法学部'), ('rigaku', '理学部')])
    is_japanese = BooleanField('日本人？:')
    message = TextAreaField('メッセージ:')
    submit = SubmitField('送信')

@app.route('/user_regist', methods=['GET', 'POST'])
def index():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['birthday'] = form.birthday.data
        session['gender'] = form.gender.data
        session['major'] = form.major.data
        session['nationality'] = '日本人' if \
            form.is_japanese.data else '外国人'
        session['message'] = form.message.data
        return redirect(url_for('show_user'))


    return render_template('user_regist.html', form=form)

@app.route('/show_user')
def show_user():
    return render_template('show_user.html')


if __name__ == '__main__':
    app.run(debug=True)
