

from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.widgets import HiddenInput, TextArea
from wtforms.validators import Optional
from flask.ext.wtf import Form

from .models import Post


_field_args = {
    'id': {
        'widget': HiddenInput(),
        'validators': [Optional()]
    },
    'parent_id': {
        'widget': HiddenInput(),
        'validators': [Optional()]
    },
    'text': {
        'widget': TextArea()
    },
}

PostForm = model_form(
    Post,
    base_class=Form,
    only=['id', 'title', 'text'],
    field_args=_field_args,
    exclude_pk=False,
    exclude_fk=False,
)
