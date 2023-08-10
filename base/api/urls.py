from django.urls import path
from .view import * 

urlpatterns = [
    path('', getRoutes),
    path('rooms/', getRooms),
    path('rooms/<int:pk>/', getRoom),
]