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
        response = Response()

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response

    def route(self, path):
        """explaine here..."""
        print('\nin route.\n')
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper
