from django.urls import path
from . import views

urlpatterns = [
    path('', views.anytime, name='anytime')
]