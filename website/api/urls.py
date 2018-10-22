from django.conf.urls import url
from . import views

urlpatterns = [
 # finds the car just by id. will expand later to find based on name
 url(r'carByID$', views.carByID, name='carByID'),
 url(r'search$', views.search, name='search'),
  url(r'customerByID$', views.customerByID, name='customerByID'),
 url(r'customer$', views.customer, name='customer')
]
