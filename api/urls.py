from django.urls import path
from . import views
urlpatterns = [
    path('',views.apitest , name="api-test") ,
    path('todos/', views.TodoItemview.as_view(), name="todo-list"),
    path('todos/<int:pk>/', views.TodoItemview.as_view(), name="todo-detail"),
    
]