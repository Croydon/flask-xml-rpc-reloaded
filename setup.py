"""
Flask-XML-RPC-Re
----------------
Flask-XML-RPC-Re adds XML-RPC support to Flask. This way, you can provide simple
APIs easily accessible from almost any programming language.

Links
`````

* `documentation <https://croydon.github.io/flask-xml-rpc-reloaded/>`_
* `development <https://github.com/Croydon/flask-xml-rpc-reloaded>`_

"""

from setuptools import setup
from codecs import open
import os


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='Flask-XML-RPC-Re',
    version='0.2.0a1',
    url='https://github.com/Croydon/flask-xml-rpc-reloaded',
    license='MIT',
    author='Matthew "LeafStorm" Frazier',
    author_email='flask@go-dev.de',
    description='Adds support for creating XML-RPC APIs to Flask',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['flask_xmlrpcre', 'flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    extras_require={
        'dev': ['sphinx'],
        'test': ['nose'],
    },
    test_suite='nose.collector',
    keywords='XML-RPC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
