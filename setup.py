"""
Flask-XML-RPC-Re
-------------
Flask-XML-RPC-Re adds XML-RPC support to Flask. This way, you can provide simple
APIs easily accessible from almost any programming language.

Links
`````

* `documentation <http://packages.python.org/Flask-XML-RPC-Re>`_
* `development <https://github.com/Croydon/flask-xml-rpc-reloaded>`_

"""

from setuptools import setup

setup(
    name='Flask-XML-RPC-Re',
    version='0.1.4',
    url='https://github.com/Croydon/flask-xml-rpc-reloaded',
    license='MIT',
    author='Matthew "LeafStorm" Frazier',
    author_email='flask@go-dev.de',
    description='Adds support for creating XML-RPC APIs to Flask',
    long_description=__doc__,
    packages=['flask_xmlrpcre', 'flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    tests_require='nose',
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
