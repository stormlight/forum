

from flask import Blueprint


discussions = Blueprint('discussions', __name__,
                        url_prefix='/discussions',
                        template_folder='templates/')
