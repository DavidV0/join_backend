from rest_framework import generics
from .models import Todo, Contact
from .serializers import TodoSerializer,ContactSerializer

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset =  Todo.objects.all()
       
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
    
class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset =  Contact.objects.all()    

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset =  Contact.objects.all()    