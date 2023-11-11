from django.urls import path
from . import views

urlpatterns = [
    path('foo', views.index, name='index')
]
