from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5, Bootstrap
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = "music-heals-me"
email = "admin@email.com"
password = "12345678"

class LoginForm(FlaskForm):
    name = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        pwd = form.password.data
        if username == email and pwd == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
