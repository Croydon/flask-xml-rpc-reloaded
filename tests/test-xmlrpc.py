"""
test-xmlrpc.py
==============
Tests for Flask-XML-RPC-Re.

:copyright: (c) 2010 by Matthew "LeafStorm" Frazier.
:license: MIT, see LICENSE for more details.
"""

import unittest
from flask import Flask
from flask_xmlrpcre import (XMLRPCHandler, XMLRPCNamespace, Fault,
                             dump_method_call, load_method_response,
                             test_xmlrpc_call, XMLRPCTester)

import xmlrpc.client as xmlrpclib

def hello(name='world'):
    if not name:
        raise Fault('unknown_recipient', "I need someone to greet!")
    return "Hello, %s!" % name


class TestHandler(unittest.TestCase):
    def test_creation(self):
        handler = XMLRPCHandler('api')
        self.assertEqual(handler.endpoint_name, 'api')
        self.assertIn('system.listMethods', handler.funcs)
        self.assertIn('system.methodHelp', handler.funcs)
        self.assertIn('system.methodSignature', handler.funcs)
        self.assertNotIn('system.multicall', handler.funcs)

    def test_instance(self):
        handler = XMLRPCHandler('api')
        obj = object()
        handler.register_instance(obj)
        self.assertIs(handler.instance, obj)

    def test_connect(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        app_handler = app.view_functions[handler.endpoint_name].__self__
        self.assertIs(app_handler, handler)

    def test_register(self):
        handler = XMLRPCHandler('api')
        handler.register(hello)
        self.assertIs(handler.funcs['hello'], hello)
        handler.register(hello, 'hi')
        self.assertIs(handler.funcs['hi'], hello)

    def test_namespaces(self):
        handler = XMLRPCHandler('api')
        ns = handler.namespace('ns')
        self.assertEqual(ns.prefix, 'ns')
        self.assertIs(ns.handler, handler)
        misc = ns.namespace('misc')
        self.assertEqual(misc.prefix, 'ns.misc')
        self.assertIs(misc.handler, handler)

        misc.register(hello)
        self.assertIs(handler.funcs['ns.misc.hello'], hello)

    def test_call(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        handler.register(hello)

        data = dump_method_call('hello', 'Steve')
        client = app.test_client()
        rv = client.post('/api', data=data, content_type='text/xml')
        res = load_method_response(rv.data)
        self.assertEqual(res, 'Hello, Steve!')


class TestTestingUtils(unittest.TestCase):
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
        self.assertEqual(
            dump_method_call('hello', 'world'),
            xmlrpclib.dumps(('world',), methodname='hello')
        )

    def test_load_method_response(self):
        self.assertEqual(
            load_method_response(self.METHOD_RESPONSE),
            'Hello, world!'
        )

    def test_test_xmlrpc_call(self):
        handler = XMLRPCHandler('api')
        app = Flask(__name__)
        handler.connect(app, '/api')
        handler.register(hello)

        self.assertEqual(
            test_xmlrpc_call(app.test_client(), '/api', 'hello'),
            'Hello, world!'
        )

if __name__ == '__main__':
    unittest.main()
