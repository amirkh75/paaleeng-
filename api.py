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

    def find_handler(self, request_path):
        """explaine here..."""
        for path, handler in self.routes.items():
            if path == request_path:
                return handler


    def handle_request(self, request):
        """explaine here..."""
        response = Response()

        handler = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)
        
        return response

    def route(self, path):
        """explaine here..."""
        print('\nin route.\n')
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def default_response(self, response):
        """explaine here..."""
        response.status = 404
        response.text = '<h1>you lost here? you can got <a href="/"> here </a></h1>'
