from django.contrib import admin

# Register your models here.
from main.models import Doctor, Comment, Spec

admin.site.register(Doctor)
admin.site.register(Comment)
admin.site.register(Spec)
