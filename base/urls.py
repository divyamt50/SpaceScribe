from django.urls import path
from .views import *

urlpatterns = [
    path('',homeView.as_view(),name = "home"),
    path('room/<int:pk>/', room, name = "room"),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<int:pk>/', UpdateRoom , name = 'update-room'),
    path('delete-room/<int:pk>/', DeleteRoom, name = 'delete-room'),
    path('login/', loginPage, name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('register/', registerUser, name = "register"),
    path('delete-message/<int:pk>/', DeleteMessage, name = 'delete-message'),
    path('profile/<int:pk>/', userProfile, name = "user-profile"),
    path('update-user/', updateUser, name = "update-user"),
    path('topics/', topicsPage, name='topics'),
    path('activity/',activityPage,name = "activity")
]
