

import re
from setuptools import setup, find_packages

from pip.req import parse_requirements


# application name
app_name = 'stormlight'

# determine version and the authors
code = open(app_name + '/__init__.py', 'r').read(1000)
version = re.search(r'__version__ = \'([^\']*)\'', code).group(1)
authors = eval(re.search(r'__authors__ = (\[[^\]\[]*\])', code).group(1))

# read requirements
parsed_req = parse_requirements('requirements.txt')
install_req = [str(line.req) for line in parsed_req]


setup(
    name=app_name,
    version=version,
    author=', '.join(authors),
    py_modules=['manage'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=install_req,
    entry_points={
        'console_scripts': [
            app_name + ' = manage:manager.run',
        ],
    },
)
