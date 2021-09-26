# app.py


from api import API
from urls import urlpatterns


app = API()
urlpatterns(app)

def custom_exception_handler(request, response, exception):
    """explaine here..."""
    response.text = '<h1>oops.somthing goes wrong.</h1>'

app.add_exception_handler(custom_exception_handler)
