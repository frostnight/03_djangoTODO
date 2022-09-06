from django.urls import path

from drf_todo.views import TodosAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
]
