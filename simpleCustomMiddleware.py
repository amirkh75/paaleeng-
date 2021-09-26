from middleware import Middleware


class SimpleCustomMiddleware(Middleware):
    """explaine here..."""

    def process_request(self, request):
        print("Processing request", request.url)
        print('\n\n\n')
    
    def process_response(self, request, response):
        print("Processing response", request.url)
        print('\n\n\n')
