# in your app's urls.py
from django.urls import path
from . import views

app_name = 'kandamul'

urlpatterns = [
    path('', views.index_view, name='home'),
]