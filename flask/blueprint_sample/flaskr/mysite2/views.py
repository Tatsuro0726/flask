from flask import Blueprint, render_template

mysite2_bp = Blueprint('mysite2', __name__, url_prefix='/site2')

# url: http://----/site2/hello
@mysite2_bp.route('/hello')
def hello():
    return render_template('mysite2/hello.html')

