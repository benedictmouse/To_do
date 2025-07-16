from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    """
    Serializer for TodoItem model.
    This serializer handles the serialization and deserialization of
    TodoItem instances, including the fields 'id', 'title', and 'completed'.
    """
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(default=False, allow_null=True, required=False)


    class Meta:
        model = TodoItem
        fields = (
            'id', 
            'title', 
            'description',
            'completed'
        )
