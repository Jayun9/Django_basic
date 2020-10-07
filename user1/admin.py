from django.contrib import admin
from .models import User1
# Register your models here.

class User1Admin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User1, User1Admin)