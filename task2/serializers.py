from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import Person
class AddPersonSerializer(serializers.ModelSerializer):

    name = serializers.CharField( )

    class Meta:
        model = Person
        fields = "__all__"