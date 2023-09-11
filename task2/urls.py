from django.urls import path
from . views import AddPerson, ModifyPerson

urlpatterns = [
    path('', AddPerson.as_view(), name="Add Person"),
    path('<int:pk>/', ModifyPerson.as_view(), name="Modify Person"),
]
