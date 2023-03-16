from django.urls import re_path

from . import views

urlpatterns = [
  re_path('todos/', views.TodoListView.as_view()),
  re_path('todos/<int:id>/', views.TodoListView.as_view()),
]

