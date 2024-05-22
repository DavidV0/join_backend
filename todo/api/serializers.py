# kanban/serializers.py
from rest_framework import serializers
from .models import Todo, Contact, Subtask

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Todo
        fields = '__all__'
