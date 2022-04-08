from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_Page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('update/<str:pk>', views.update),
    path('view/', views.view),
    path('delete/', views.delete),

    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('book/', views.books, name="book"),
    path('author/', views.authors, name="author"),
    path('publisher/', views.publishers, name="publisher")



]
