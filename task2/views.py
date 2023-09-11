from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . models import Person
from . serializers import AddPersonSerializer
# Create your views here.

class AddPerson(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = AddPersonSerializer

class ModifyPerson(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = AddPersonSerializer

