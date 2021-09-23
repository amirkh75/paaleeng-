# app.py

""" this componented after api.py
def app(environ, start_response):
    \""" this app speaks with http web server with wsgi rules.\"""
    response_body = b'Hello, world!'
    status = '200 OK'
    start_response(status, headers=[])
    return iter([response_body])
"""

from api import API

app = API()


@app.route('/')
def home(request, response):
    """ explains the current..."""
    response.text = '<h2>Hello from the HOME page.<\h2>'

@app.route('/about')
def about(request, response):
    """ explains the current..."""
    response.text = '<h2>Hello from the ABOUT page.<\h2>'



print(app.routes)