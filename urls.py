# urls.py


from views import home, about, greeting, BookHandler


def urlpatterns(app):
    app.add_route( '/', home)
    app.add_route( '/about', about)
    app.add_route( '/hello/{name}', greeting)
    app.add_route( '/book', BookHandler)
