# kanban/views.py
from rest_framework import generics
from .models import Todo, Contact, Subtask
from .serializers import TodoSerializer, ContactSerializer, SubtaskSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
       
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class SubtaskList(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()

    def perform_create(self, serializer):
        parent_task_id = self.request.data.get('parent_task')
        parent_task = Todo.objects.get(id=parent_task_id)
        serializer.save(parent_task=parent_task)

class SubtaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
