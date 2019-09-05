from django.db import models
from django.contrib.auth.middleware import RemoteUserMiddleware

# Create your models here.

class Post(models.Model,RemoteUserMiddleware):
    user = "Dupa"


    def __str__(self):
        return self.name