from django.urls import path 
from . import views

urlpatterns = [
      path('', views.input, name="input"),
      path('submit', views.submit, name="submit"),
]