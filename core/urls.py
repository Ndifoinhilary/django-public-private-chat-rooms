from django.urls import path

from core import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
]