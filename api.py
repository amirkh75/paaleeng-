# api.py

from webob import Request, Response

class API:
    """explaine here..."""

    def __init__(self):
        """explaine here..."""
        self.routes = {}

    def __call__(self, environ, start_response):
        """explaine here..."""

        client_address = environ.get('REMOTE_ADDR')
        print(f'\nNew Call from { client_address }\n')

        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        """explaine here..."""
        user_agent = request.environ.get('HTTP_USER_AGENT', 'No User Agent Found')

        response = Response()
        response.text = f'<h1>Hello, my friend with this user agent: {user_agent}<\h1>.'

        return response

    def route(self, path):
        """explaine here..."""
        print('\nin route.\n')
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper
