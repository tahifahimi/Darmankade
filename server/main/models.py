from django.db import models

# Create your models here.
from authentication.models import User


class Spec(models.Model):
    name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)


class Doctor(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE, related_name='doctor')
    spec = models.ForeignKey(Spec, on_delete=models.PROTECT, related_name='doctors')
    number = models.CharField(max_length=32)
    online_pay = models.BooleanField()
    experience_years = models.SmallIntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=16)
    week_days = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='comments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField()
    rate = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
