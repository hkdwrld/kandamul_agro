from django.urls import path
from .views import HomeView  # Import your class-based view

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
   
]
