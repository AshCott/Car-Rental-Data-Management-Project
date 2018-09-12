from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'), #base url, localhost:8000
 url('search/', views.search, name='search'), # search url, shows on localhost:8000/search/
url('employee_home/', views.employee_home, name='employee_home'), # redirects employee to their homepage after logging on, shows on localhost:8000/employee_home/
url('logout/', views.logout, name='logout'), # redirects employee to the logout page, shows on localhost:8000/logout/
url('car_details/(\d+)', views.car_details, name='car_details') # search url, shows on localhost:8000/car_details/
]
