
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Length, Required


class CreateForm(Form):
    name = StringField(
        'Name',
        [Length(min=2, max=25), Required()]
    )

    description = TextAreaField(
        'Description',
        [Length(min=5, max=255)]
    )