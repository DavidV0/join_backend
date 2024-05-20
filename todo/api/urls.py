from django.urls import path
from .views import TodoList, TodoDetail, ContactList, ContactDetail

urlpatterns = [
    path('todos/', TodoList.as_view()),
    path('todos/<int:pk>/', TodoDetail.as_view()),
    path('contacts/', ContactList.as_view()),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
    
]