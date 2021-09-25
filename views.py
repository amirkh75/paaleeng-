# views.py


def home(request, response):
    """ function based and class based views (our handlers) """
    response.text = '<h1>Hello from the HOME page.</h1>'


def about(request, response):
    """ explains the current..."""
    response.text = '<h1>Hello from the ABOUT page.</h1>'


def greeting(request, response, name):
    """explains here."""
    response.text = f'<h1> Hello, {name} </h1>'


class BookHandler:
    def get(self, request, response):
        response.text = f'<h1> Books Page</h1>'
    
    def post(self, request, response):
        response.text = f'<h1>Endpoint to create a new book</h1>'

def template_handler(request, response, app):
    """explaine here..."""
    print(str(type(app)))
    print('\n\n\n')
    response.body = app.template(template_name="index.html", context={"name": "paaleeng#", "title": "best framework ever"}).encode()