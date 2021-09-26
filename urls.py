# urls.py


from views import home, about, greeting, BookHandler, template_handler, exception_throwning_handler


def urlpatterns(app):
    app.add_route( '/', home)
    app.add_route( '/about', about)
    app.add_route( '/hello/{name}', greeting)
    app.add_route( '/book', BookHandler)
    app.add_route( '/template', template_handler)
    app.add_route( '/home', exception_throwning_handler)
