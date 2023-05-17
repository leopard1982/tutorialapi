from django.contrib import admin
from django.urls import path
from tutorial1.views import hello_world, tampilUser


urlpatterns = [
    path('', hello_world, name="hello_world"),
    path('v/user/',tampilUser,name="tampilUser")
]
