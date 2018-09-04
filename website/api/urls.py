from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'sample$', views.sample, name='sample'), # search url, shows on localhost:8000/search/
 url(r'sampleCar$', views.sampleCar, name='sampleCar')
]
