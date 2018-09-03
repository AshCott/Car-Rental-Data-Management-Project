from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'), #base url
 url('search/', views.search, name='search')
]
