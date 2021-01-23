from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

# --------------------
# UserInfoクラス作成
# --------------------
class UserInfo:

    def __init__(self, number, name, age, gender, major, picture_path):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.picture_path = picture_path

# -------------------------
# memberを作成
# -------------------------
member = [
    UserInfo(0, 'Taro', 20, 'men', 'engineering', '/image/pictures/taro.jpg'),
    UserInfo(1, 'Jiro', 19, 'men', 'science', '/image/pictures/jiro.jpg'),
    UserInfo(2, 'Ryoko', 21, 'woman', 'law', '/image/pictures/ryoko.jpg'),
    UserInfo(3, 'Hanako', 22, 'woman', 'economics', '/image/pictures/hanako.jpg')
]

# メインページ
@app.route('/')
def main():
    return render_template('main.html')

# メンバ一覧ページ
@app.route('/memberlist')
def load_member_list():
    return render_template('memberlist.html', member_list = member)

# メンバーの詳細
@app.route('/memberlist/<int:member_number>')
def member_detail(member_number):
    for user in member:
        if user.number == member_number:
            return render_template('member_detail.html', user=user)
    return redirect(url_for('main'))

@app.route('/terms')
def terms_of_service():
    return render_template('terms.html')

# --------------------------
# エラーハンドル
# --------------------------
@app.errorhandler(404)
def redirect_main_page(error):
    return redirect(url_for('main')), 404



if __name__ == "__main__":
    app.run(debug=True)