

from wtforms.widgets import HiddenInput, TextArea
from wtforms.validators import Optional
from wtforms_alchemy import ModelForm

from .models import Forum


class ForumForm(ModelForm):
    """Forum form.
    """
    class Meta:
        model = Forum
        only = ['id', 'parent_id', 'title', 'description']
        strip_string_fields = True
        validators = {
            'id': Optional(),
            'parent_id': Optional(),
        }
