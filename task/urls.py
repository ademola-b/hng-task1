from django.urls import path
from .views import Task
urlpatterns = [
    path('', Task.as_view(), name="Task 1"),
]
