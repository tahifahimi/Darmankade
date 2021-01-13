from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    # username, first name, last name and email is built in
    mobile = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def type(self):
        return self.groups.first().name if self.groups.first() else "client"

