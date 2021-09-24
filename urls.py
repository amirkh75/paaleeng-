from api import API
from app import home, about, greeting, BookHandler


app = API()


app.add_route( '', home)
app.add_route( '/about', about)
app.add_route( '/hello/{name}', greeting)
app.add_route( '/book', BookHandler)