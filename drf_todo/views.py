from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_todo.models import Todo
from drf_todo.serializers import TodoSimpleSerializer


class TodosAPIView(APIView):

    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
