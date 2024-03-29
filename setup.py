# python setup.py sdist bdist_wheel
# twine upload dist/*
from setuptools import setup, find_packages
# import codecs
import os

def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

VERSION = '0.0.21'
DESCRIPTION = 'This is a simple package to help musicians to general functions.'
LONG_DESCRIPTION = 'www.charlesneimog.com'

# Setting up
setup(
    name="om_py",
    version=VERSION,
    author="Charles K. Neimog",
    author_email="<charlesneimog@outlook.com>",
    url = 'https://github.com/charlesneimog/OM_py',
    description=DESCRIPTION,
    long_description = (read('README.md') + '\n\n' + read('COPYING.rst') ),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['html_to_json', 'python-osc'],
    keywords=['python', 'CAC', 'OpenMusic'],
    classifiers=[
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
