
from django.http import JsonResponse
from rest_framework.response import Response
from api.serializers import TodoItemSerializer
from api.models import TodoItem
from rest_framework.views import APIView


class TodoItemview (APIView):
   
    def get(self, request, pk=None):
        if pk :
        
            todos = TodoItem.objects.get(id=pk)
            serializer = TodoItemSerializer(todos, many=False)
            return Response(serializer.data)
        else:
            todos = TodoItem.objects.all()
            serializer = TodoItemSerializer(todos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):

        todos = TodoItem.objects.get(id=pk)
        todos.delete()
        return Response(status=204)
    def patch(self, request, pk):
        try:
            todos = TodoItem.objects.get(id=pk)
            serializer = TodoItemSerializer(todos, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TodoItem.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request, pk):
        try:
            todos = TodoItem.objects.get(id=pk)
            serializer = TodoItemSerializer(todos, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TodoItem.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)



def apitest(request):
    return JsonResponse({"message": "API BASE POINT"})

