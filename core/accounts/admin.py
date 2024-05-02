from django.contrib import admin
from .models.user import CustomUser
from .models.profile import Profile

# Register your models here.

admin.site.register(Profile)