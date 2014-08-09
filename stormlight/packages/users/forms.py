
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Length


class SignupForm(Form):
    username = StringField(
        'Username',
        [Length(min=3, max=25)]
    )

    email = StringField(
        'Email Address', 
        [Length(min=6, max=35)]
    )

    repeat_email = StringField(
        'Repeat Email Address', 
        [Length(min=6, max=35)]
    )

    password = PasswordField(
        'Password', 
        [Length(min=6, max=35)]
    )

    repeat_password = PasswordField(
        'Repeat Password', 
        [Length(min=6, max=35)]
    )