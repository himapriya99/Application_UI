from django.urls import path 
from . import views

urlpatterns = [
      path('', views.input, name="input"),
      path('submit', views.submit, name="submit"),
      path('scope_alert',views.scope_alert, name="scope_alert"),
      path('code_alert',views.code_alert, name="code_alert"),
      path('download',views.download,name="download"),
]
