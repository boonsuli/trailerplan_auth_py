# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app_python.models import User

admin.site.register(User, UserAdmin)
