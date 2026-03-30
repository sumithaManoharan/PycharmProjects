from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()], render_kw={"class": "form-control"})
    subtitle = StringField('Subtitle', validators=[DataRequired()], render_kw={"class": "form-control"})
    body = CKEditorField("Blog Content")
    author = StringField('Author', validators=[DataRequired()], render_kw={"class": "form-control"})
    img_url = StringField('Image URL', validators=[DataRequired(), URL()], render_kw={"class": "form-control"})
    submit = SubmitField('SUBMIT POST', render_kw={"class": "btn btn-primary"})


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign Me up!', render_kw={"class": "btn btn-primary"})



# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('LOGIN', render_kw={"class": "btn btn-primary"})


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    name = StringField('Name', default="User", render_kw={"class": "form-control"})
    comment = CKEditorField('Comment', render_kw={"class": "form-control"})
