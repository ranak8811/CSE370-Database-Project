from django.contrib import admin
from django.contrib.auth import views as auth_views
# Register your models here.
from authentication.models import Task 
admin.site.register(Task)