from rest_framework import serializers
from .models import Todo, Contact, Subtask

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('__all__')
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')
        
        
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ('__all__')