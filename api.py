# api.py

from webob import Request, Response
from parse import parse


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
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        
        return None, None


    def handle_request(self, request):
        """explaine here..."""
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        
        return response

    def route(self, path):
        """explaine here..."""

        if path in self.routes:
            raise AssertionError(f"\n\nSuch route already exists.({path})\n\n")
        # or -> asset path ot in self.routes, "Such route already exists."
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def default_response(self, response):
        """explaine here..."""
        response.status = 404
        response.text = '<h1>you lost here? you can got <a href="/"> here </a></h1>'
