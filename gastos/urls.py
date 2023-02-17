from django.urls import path
from . import views

urlpatterns = [
    path('conta/', views.contas, name='conta'),
    
]