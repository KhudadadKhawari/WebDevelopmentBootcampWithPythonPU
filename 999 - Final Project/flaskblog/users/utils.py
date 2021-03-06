import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ ,file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pic', picture_fn)
    output_size = (200,200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset', sender='noreply@seferyak.com',recipients=[user.email])
    msg.body = f"""Click on the below link to reset your password:
{url_for('users.reset_token', token=token, _external = True)}

Ignore this email if you didn't requeseted for a password reset
    """
    mail.send(msg)