# app.py


from api import API
from urls import urlpatterns


app = API()
urlpatterns(app)

