from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<int:year>/')
def index(year):
    return render_template(
        'leap.html',
        age=5,
        year=year,
    )