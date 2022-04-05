from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('update/<str:pk>', views.update),
    path('view/', views.view),
    path('delete/', views.delete),
    path('', views.home),
]
