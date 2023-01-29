from django.urls import path
from . import views

urlpatterns = [
    path('', views.Preview, name='Preview'),
]
