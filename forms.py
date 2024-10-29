from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegistrationForm(FlaskForm):
    email = EmailField("Enter Your Email", validators=[DataRequired()], render_kw={'style': 'width: 500px'})
    name = StringField("Enter Your Name", validators=[DataRequired()], render_kw={'style': 'width: 300px'})
    password = PasswordField("Create Password", validators=[DataRequired(), Length(min=6)],
                             render_kw={'style': 'width: 300px'})
    submit = SubmitField("Register")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Enter your Email", validators=[DataRequired()], render_kw={'style': 'width: 500px'})
    password = PasswordField("Enter your Password", validators=[DataRequired()], render_kw={'style': 'width: 500px'})
    submit = SubmitField("Log In")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comments = CKEditorField("Comments", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
