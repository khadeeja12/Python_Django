from django.urls import path
# import from current module and it reference the view function
from . import views 

#URLConf
urlpatterns=[
    path('hello/',views.say_hello),
    path('', views.home),
]