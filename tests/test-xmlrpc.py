# -*- coding: utf-8 -*-
"""
test-xmlrpc.py
==============
Tests for Flask-XML-RPC-Re.

:copyright: (c) 2010 by Matthew "LeafStorm" Frazier.
:license: MIT, see LICENSE for more details.
"""

from flask import Flask
from flask_xmlrpcre import (XMLRPCHandler, XMLRPCNamespace, Fault,
                             dump_method_call, load_method_response,
                             test_xmlrpc_call, XMLRPCTester)

import sys
PY2 = sys.version_info[0] == 2

if PY2:
    import xmlrpclib
else:
    import xmlrpc.client as xmlrpclib

def hello(name='world'):
    if not name:
        raise Fault('unknown_recipient', "I need someone to greet!")
    return "Hello, %s!" % name


class TestHandler(object):
    def test_creation(self):
        handler = XMLRPCHandler('api')
        assert handler.endpoint_name == 'api'
        assert 'system.listMethods' in handler.funcs
        assert 'system.methodHelp' in handler.funcs
        assert 'system.methodSignature' in handler.funcs
        assert 'system.multicall' not in handler.funcs

    def test_instance(self):
        handler = XMLRPCHandler('api')
        obj = object()
        handler.register_instance(obj)
        assert handler.instance is obj

    def test_connect(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        if PY2:
            app_handler = app.view_functions[handler.endpoint_name].im_self
        else:
            app_handler = app.view_functions[handler.endpoint_name].__self__
        assert app_handler is handler

    def test_register(self):
        handler = XMLRPCHandler('api')
        handler.register(hello)
        assert handler.funcs['hello'] is hello
        handler.register(hello, 'hi')
        assert handler.funcs['hi'] is hello

    def test_namespaces(self):
        handler = XMLRPCHandler('api')
        ns = handler.namespace('ns')
        assert ns.prefix == 'ns'
        assert ns.handler is handler
        misc = ns.namespace('misc')
        assert misc.prefix == 'ns.misc'
        assert misc.handler is handler

        misc.register(hello)
        assert handler.funcs['ns.misc.hello'] is hello

    def test_call(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        handler.register(hello)

        data = dump_method_call('hello', 'Steve')
        client = app.test_client()
        rv = client.post('/api', data=data, content_type='text/xml')
        res = load_method_response(rv.data)
        assert res == 'Hello, Steve!'


class TestTestingUtils(object):
    METHOD_RESPONSE = '''\
<?xml version='1.0'?>
<methodResponse>
<params>
<param>
<value><string>Hello, world!</string></value>
</param>
</params>
</methodResponse>
'''

    def test_dump_method_call(self):
        assert (dump_method_call('hello', 'world') ==
                xmlrpclib.dumps(('world',), methodname='hello'))

    def test_load_method_response(self):
        assert (load_method_response(self.METHOD_RESPONSE) ==
                'Hello, world!')

    def test_test_xmlrpc_call(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        handler.register(hello)

        assert (test_xmlrpc_call(app.test_client(), '/api', 'hello') ==
                'Hello, world!')
