from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def name_validate(value):
    if not isinstance(value, str):
        raise ValidationError("Only Strings are allowed")


class Person(models.Model):
    name = models.CharField(unique=True, max_length=50, validators=[name_validate])
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=1000)
