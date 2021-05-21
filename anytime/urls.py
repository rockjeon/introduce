from django.urls import path
from . import views

app_name = 'anytime'
urlpatterns = [
    path('', views.anytime, name='main'),
    path('create', views.create, name='create')
]