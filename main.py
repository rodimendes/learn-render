from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


application = Flask(__name__)
Bootstrap(application)
application.secret_key = 'mykey'

class Subscribe(FlaskForm):
    name = StringField(label='Name:', validators=[DataRequired(message='We need to be a little closer. How can I call you?')])
    age = IntegerField(label='Age:')
    email = EmailField(label='E-mail:', validators=[DataRequired(message='Write your best e-mail. We will not send unnecessary e-mails.'), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(message='For your security, this field cannot be left blank.'), Length(min=8, max=15, message='Your password must be between 8 and 15 characters')])
    submit = SubmitField(label='Subscribe')

@application.route('/', methods=['POST', 'GET'])
def home():
    myform = Subscribe()
    print(request.method)
    if myform.validate_on_submit():
        if myform.name.data == 'Rodrigo':
            return render_template('success.html', form=myform)
        else:
            return render_template('denied.html')

    return render_template('index.html', form=myform)


if __name__ == '__main__':
    application.run(debug=True)