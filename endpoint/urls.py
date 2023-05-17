from django.contrib import admin
from django.urls import path
from endpoint.views import viewAllUser, viewDetailUser

urlpatterns = [
    path('1/', viewAllUser, name="viewAllUser"),
    path('1/<int:pk>/',viewDetailUser,name="viewDetailUser"),
]
