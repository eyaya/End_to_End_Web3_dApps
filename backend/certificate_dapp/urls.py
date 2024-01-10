# todos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.ListAccount.as_view()),
    path('<int:pk>/', views.DetailAccount.as_view()),
]