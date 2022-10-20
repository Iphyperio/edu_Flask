from textwrap import TextWrapper
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key='you_need_a_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():


    return render_template(
        'message.html',
        message=server_message
    )


class MessageForm(FlaskForm):
    name=StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators = [DataRequired()])
    submit = SubmitField("submit")
