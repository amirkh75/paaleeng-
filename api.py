# api.py

from webob import Request, Response
from parse import parse
import inspect
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter


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
            if inspect.isclass(handler):
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError('Method not allowed', request.method)

            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        
        return response

    def add_route(self, path, handler):
        """explaine here..."""
        assert path not in self.routes, f"\n\nSuch route already exists.({path})\n\n"
        self.routes[path] = handler

    def route(self, path):
        """explaine here..."""

        def wrapper(handler):
            self.add_route(path, handler)
            return handler
        
        return wrapper

    def default_response(self, response):
        """explaine here..."""
        response.status = 404
        response.text = '<h1>you lost here? you can go <a href="/">here</a>.</h1>'

    def test_session(self, base_url='http://testserver'):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session