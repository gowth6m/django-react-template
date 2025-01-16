from django.db import models
from django.contrib.auth.models import User


class AppUser(User):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    pass
