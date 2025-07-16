from django.contrib import admin
from .models import TodoItem 


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):


    list_display = ('id', 'title', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)
    ordering = ('-id',)