from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField	
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=5,max= 20 )])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Already Taken Please choose another username')

    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email:
            raise ValidationError('Email Already Taken Please Use another Email')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=5,max= 20 )])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture  = FileField('Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Submit Changes')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if username.data != current_user.username:
            if user:
                raise ValidationError('Username Already Taken Please choose another username')

    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if email.data != current_user.email:
            if user_email:
                raise ValidationError('Email Already Taken Please Use another Email')

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Reset Password')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')