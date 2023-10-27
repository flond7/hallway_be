from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'authorized_aa', 'authorized_peg']  # Add your custom fields here

admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.
