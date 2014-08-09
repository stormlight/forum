

from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Optional, Length


class ForumForm(Form):
    """Forum form.
    """
    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Length(min=4, max=50),
        ],
    )
    description = TextAreaField(
        'Description',
        validators=[
            Optional(),
            Length(min=4),
        ],
    )
    container = BooleanField(
        'Is container?',
        default=False
    )
