from django.urls import path

from account import views

urlpatterns = [
    path('register', views.register_view, name='register'),
]