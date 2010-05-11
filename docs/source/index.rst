.. Flask-XML-RPC documentation master file, created by
   sphinx-quickstart on Mon May 10 10:44:09 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============
Flask-XML-RPC
=============

.. module:: flaskext.xmlrpc

Flask-XML-RPC is an extension for `Flask`_ that makes it easy to create APIs
based on the `XML-RPC`_ standard.

.. _Flask: http://flask.pocoo.org/
.. _XML-RPC: http://www.xmlrpc.com/


Features
========
* Easy registration of methods and namespacing
* Connects seamlessly to your Flask app
* Includes plenty of testing helpers


Install
=======
If you're using easy_install, then run this command to install Flask-XML-RPC:

.. sourcecode:: console
   
   $ easy_install Flask-XML-RPC

Or, if you're using `pip`_ (which is recommended, since it's awesome):

.. sourcecode:: console
   
   $ pip install Flask-XML-RPC

.. _pip: http://pip.openplans.org/


A Simple Example
================
This is a REALLY simple example of how to create your own API using
Flask-XML-RPC. ::

    from flask import Flask
    from flaskext.xmlrpc import XMLRPCHandler, Fault
    
    app = Flask(__name__)
    
    handler = XMLRPCHandler('api')
    handler.connect(app, '/api')
    
    @handler.register
    def hello(name="world"):
        if not name:
            raise Fault("unknown_recipient", "I need someone to greet!")
        return "Hello, %s!" % name
    
    app.run()


Namespacing
===========
Of course, the :meth:`~XMLRPCHandler.register_function` method can take a name
if you want to use dotted names, but it's easier to use namespaces. You get a
namespace by calling the :meth:`~XMLRPCHandler.namespace` method with the
prefix you want (without the dot). ::

    handler = XMLRPCHandler('api')
    blog = handler.namespace('blog')
    
    @blog.register
    def add_post(title, text):
        # do whatever...
        pass

The :obj:`add_post` function will then be available as :obj:`blog.add_post`.
You can create namespaces from namespaces, as well. ::

    blog_media = blog.namespace('media')
    
    @blog_media.register
    def delete(filename):
        # do whatever...
        pass

In this case, :obj:`delete` will be available as :obj:`blog.media.delete`.
Namespacing can help you organize your API in a logical way.


Testing Your API
================
The easiest way to test your application is with the :class:`XMLRPCTester`.
It takes a `werkzeug.TestClient` and the path to your responder. When called
with the method and params, it will marshal it, make a fake POST request to
the responder with the client, and demarshal the result for you, returning it
or a :obj:`Fault`.

If you're using a :obj:`unittest`-based setup like the one described in the
Flask documentation, you could use the :class:`XMLRPCTester` like::

    def test_hello(self):
        tester = XMLRPCTester(self.app, '/api')
        assert tester('hello') == 'Hello, world!'
        assert tester('hello', 'Steve') == 'Hello, Steve!'
        fault = tester('hello', '')
        assert fault.faultCode == 'unknown_recipient'

:class:`XMLRPCTester` is actually a wrapper for :func:`test_xmlrpc_call`,
which takes the client, responder path, method, and params.

If you prefer to marshal the XML-RPC data and make the requests yourself,
the two functions :func:`dump_method_call` and :func:`load_method_response`
are useful wrappers around the low-level :obj:`xmlrpclib` marshaling
functions.


Using Your API
==============
Practically all programming languages can use XML-RPC. In Python, you can
call XML-RPC methods with the standard library :obj:`xmlrpclib` module.

.. sourcecode:: pycon

    >>> import xmlrpclib
    >>> server = xmlrpclib.ServerProxy('http://localhost:5000/')
    >>> server.hello()
    'Hello, world!'
    >>> server.hello('Steve')
    'Hello, Steve!'

For other languages, please check their documentation.


API Documentation
=================
.. autoclass:: flaskext.xmlrpc.XMLRPCHandler
   :members:

.. autoclass:: flaskext.xmlrpc.XMLRPCNamespace
   :members:

Testing API
-----------
.. autoclass:: flaskext.xmlrpc.XMLRPCTester
   :members:

.. autofunction:: flaskext.xmlrpc.test_xmlrpc_call

.. autofunction:: flaskext.xmlrpc.dump_method_call

.. autofunction:: flaskext.xmlrpc.load_method_response
