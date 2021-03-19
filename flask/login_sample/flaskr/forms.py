from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User


class LoginForm(Form):
    email = StringField('メール: ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class RegisterForm(Form):
    email = StringField('メール: ', validators=[DataRequired(), Email()])
    username = StringField('名前: ', validators=[DataRequired()])
    password = PasswordField(
        'パスワード: ', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しまっせん')]
        )
    password_confirm = PasswordField('パスワード確認: ', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('メールアドレスはすでに登録されています。')