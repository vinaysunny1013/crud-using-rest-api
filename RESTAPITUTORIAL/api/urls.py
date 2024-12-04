from django.contrib import admin
from django.urls import path,include
from .views import get_users, create_user,user_detail
urlpatterns = [
    path('users/', get_users, name="get_users"),
    path('users/create', create_user, name="create_user"),
    path('users/<int:pk>', user_detail, name=" user_detail")
]
