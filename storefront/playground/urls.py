from django.urls import path 
from . import views

# urlpatterns acts as our URLConf module (url configuration)
urlpatterns = [
    path('hello/', views.say_hello)
]