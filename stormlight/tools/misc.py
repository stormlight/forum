
"""
Miscellaneous
=============

"""

import re


def underscore(string):
    """Converts input to under_scored string."""
    string = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', string).lower()
