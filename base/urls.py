from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-rr"),
    path('update-room/<str:pk>', views.updateRoom, name="update-rr"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-rr"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]