from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('')

if __name__ == "__main__":
    app.run(debug=True)