from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'), #base url, localhost:8000
 url('search/', views.search, name='search') # search url, shows on localhost:8000/search/
]
