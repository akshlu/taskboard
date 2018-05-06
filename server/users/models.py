from django.db import models
from django.contrib.auth import models as auth_models


class Person(models.Model):
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
