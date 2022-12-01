from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.fun1, name="media.html")
]
