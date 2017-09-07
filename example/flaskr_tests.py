# -*- coding: utf-8 -*-
"""
    Flaskr Tests
    ~~~~~~~~~~~~

    Tests the Flaskr application.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
import flaskr
import unittest
import tempfile
from flask_xmlrpcre import XMLRPCTester, Fault


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Before each test, set up a blank database"""
        self.db_fd, flaskr.DATABASE = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        """Get rid of the database again after each test."""
        os.close(self.db_fd)
        os.unlink(flaskr.DATABASE)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    # testing functions

    def test_empty_db(self):
        """Start with a blank database"""
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def test_login_logout(self):
        """Make sure login and logout works"""
        rv = self.login(flaskr.USERNAME, flaskr.PASSWORD)
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login(flaskr.USERNAME + 'x', flaskr.PASSWORD)
        assert 'Invalid username' in rv.data
        rv = self.login(flaskr.USERNAME, flaskr.PASSWORD + 'x')
        assert 'Invalid password' in rv.data

    def test_messages(self):
        """Test that messages work"""
        self.login(flaskr.USERNAME, flaskr.PASSWORD)
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

    def test_xmlrpc(self):
        """Verify that the API methods work"""
        tester = XMLRPCTester(self.app, '/api')

        assert tester('flaskr.new_post',
            flaskr.USERNAME, flaskr.PASSWORD, 'API Post', "The API works!"
        ) is True

        assert tester('flaskr.new_post',
            flaskr.USERNAME, flaskr.PASSWORD, 'API Post 2', "Same deal."
        ) is True

        entries = tester('flaskr.get_posts')
        assert entries[0] == {'title': 'API Post', 'text': "The API works!"}
        assert entries[1] == {'title': 'API Post 2', 'text': "Same deal."}

    def test_xmlrpc_fault(self):
        """Verify that the API authenticates properly"""
        tester = XMLRPCTester(self.app, '/api')

        fault = tester('flaskr.new_post',
            '', '', 'Bad Post', "This post should not be here."
        )
        assert isinstance(fault, Fault)
        assert fault.faultCode == 'bad_credentials'


if __name__ == '__main__':
    unittest.main()
