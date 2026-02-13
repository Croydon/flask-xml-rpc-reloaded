# Flask-XML-RPC-Re (Flask-XML-RPC-Reloaded)

This is a library that lets your Flask apps provide XML-RPC APIs. A small
example is included.


## Install

``pip install flask-xml-rpc-re``


## Compatible to Flask-XML-RPC

Flask-XML-RPC-Reloaded is a fork of the original Flask-XML-RPC, which was unfortunately abandoned.
This version should be API compatible and therefore a drop-in replacement for Flask-XML-RPC.

However, this version only supports Python 3.7+.


### Differences to Flask-XML-RPC

  * Python 3 support thanks to [@Ppjet6](https://github.com/ppjet6) ([PR](https://bitbucket.org/leafstorm/flask-xml-rpc/pull-requests/2/added-python3-support-alongside-python2/diff))
  * Uses the new Flask extension naming scheme thanks to [Félix Bouliane](https://bitbucket.org/felixbouliane/) ([PR](https://bitbucket.org/leafstorm/flask-xml-rpc/pull-requests/4/use-the-new-flask-naming-scheme/diff))


## Also Thanks To

  * [Matthew "LeafStorm" Frazier](https://github.com/leafstorm) for creating the original Flask-XML-RPC
  * Armin Ronacher for the logo
  * [abompard](https://github.com/abompard) for namespace fixes ([3a88da1](https://github.com/Croydon/flask-xml-rpc-reloaded/commit/3a88da1e135b083bbcfbccbd7596dc7e7c21d2a2), [#8](https://github.com/Croydon/flask-xml-rpc-reloaded/issues/8), [#13](https://github.com/Croydon/flask-xml-rpc-reloaded/pull/13))


## Generate Docs

``pip install .[dev]``

``sphinx-build -b html docs/source docs/build/html``


## Resources

  * PyPI:                   https://pypi.org/project/Flask-XML-RPC-Re/
  * Documentation:          https://croydon.github.io/flask-xml-rpc-reloaded/
  * GitHub:                 https://github.com/Croydon/flask-xml-rpc-reloaded
  * Original (abandoned):   https://bitbucket.org/leafstorm/flask-xml-rpc/
