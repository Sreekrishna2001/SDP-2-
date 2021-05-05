from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login),
    path('register',views.Register,name="Register")
]