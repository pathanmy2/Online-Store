
from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional admin fields as needed

    def __str__(self):
        return self.user.username