import pytest


from api import API

# use 'pytest paaleeng#.py' for test.

def test_basic_route(api):
    """explaine here..."""
    @api.route('/home')
    def home(request, response):
        response.text = 'YOLO'


def test_basic_overlap_throws_exception(api):
    """explaine here..."""
    @api.route('/home')
    def home(request, response):
        response.text = 'YOLO'

    with pytest.raises(AssertionError):
        @api.route('/home')
        def home2(request, response):
            response.text = 'YOLO'

def test_palang_test_client_can_send_requests(api, client):
    """explaine here..."""
    RESPONSE_TEXT = "THIS IS COOL."
    
    @api.route('/hey')
    def cool(request, response):
        response.text = RESPONSE_TEXT

    assert client.get('http://testserver/hey').text == RESPONSE_TEXT

def test_parameterized_route(api, client):
    """explaine here..."""

    @api.route('/{name}')
    def hello(request, response, name):
        response.text = f'hey {name}'

    assert client.get('http://testserver/bob').text == 'hey bob'
    assert client.get('http://testserver/alice').text == 'hey alice'

def test_default_404_response(client):
    response = client.get('http://testserver/doesnotexist')

    assert response.status_code == 404
    assert response.text == '<h1>you lost here? you can go <a href="/">here</a>.</h1>'

"""to do list 

    test that class based handlers are working with a GET request
    test that class based handlers are working with a POST request
    test that class based handlers are returning Method Not Allowed. response if an invalid request method is used
    test that status code is being returned properly
"""