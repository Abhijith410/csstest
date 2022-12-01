from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.fun1, name="media"),
    path('messages/', views.fun2, name="message"),
    path('profile/', views.fun3, name="profile"),
]
