"""
Flask-XML-RPC
-------------
Flask-XML-RPC adds XML-RPC support to Flask. This way, you can provide simple
APIs easily accessible from almost any programming language.

Links
`````

* `documentation <http://packages.python.org/Flask-XML-RPC>`_
* `development version
  <http://bitbucket.org/leafstorm/flask-xml-rpc/get/tip.gz#egg=Flask-XML-RPC-dev>`_


"""
from setuptools import setup


setup(
    name='Flask-XML-RPC',
    version='0.1.1',
    url='http://bitbucket.org/leafstorm/flask-xml-rpc/',
    license='MIT',
    author='Matthew "LeafStorm" Frazier',
    author_email='leafstormrush@gmail.com',
    description='Adds support for creating XML-RPC APIs to Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
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
