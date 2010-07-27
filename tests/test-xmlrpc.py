# -*- coding: utf-8 -*-
"""
test-xmlrpc.py
==============
Tests for Flask-XML-RPC.

:copyright: (c) 2010 by Matthew "LeafStorm" Frazier.
:license: MIT, see LICENSE for more details.
"""
from flask import Flask
from flaskext.xmlrpc import (XMLRPCHandler, XMLRPCNamespace, Fault,
                             dump_method_call, load_method_response,
                             test_xmlrpc_call, XMLRPCTester)


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
        assert app.view_functions[handler.endpoint_name].im_self is handler
    
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
