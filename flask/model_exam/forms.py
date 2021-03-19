from wtforms import Form
from wtforms.fields import (
    HiddenField,StringField, IntegerField, TextAreaField, SubmitField
)

class CreateForm(Form):
    # 新規メンバ一と作成するためのフォーム
    name = StringField('名前は:')
    age = IntegerField('年齢は:')
    comment = TextAreaField('コメント:')
    submit = SubmitField('作成')

class UpdateForm(Form):
    # メンバー情報を更新するためのフォーム
    id = HiddenField()
    name = StringField('名前は:')
    age = IntegerField('年齢は:')
    comment = TextAreaField('コメント:')
    submit = SubmitField('更新')

class DeleteForm(Form):
    # メンバ一情報を削除するフォーム
    id = HiddenField()
    submit = SubmitField('削除')