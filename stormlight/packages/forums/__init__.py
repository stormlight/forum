

from flask import Blueprint


forums = Blueprint('forums', __name__,
                   url_prefix='/forums',
                   template_folder='templates/')
