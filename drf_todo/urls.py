from django.urls import path

from drf_todo.views import TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:pk>', TodoAPIView.as_view()),
    path('done', DoneTodosAPIView.as_view()),
    path('done/<int:pk>', DoneTodoAPIView.as_view())
]
