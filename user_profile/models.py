from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(max_length=8)

    def to_dict(self):
        data = {
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'dob' : str(self.dob),
            'email': self.user.email
        }
        return data

    def __str__(self):
        return self.user.username
