from django.contrib import admin

# Register your models here.
# code to access django admin site
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class MyUserAdmin(UserAdmin):
    # Add any additional fields you want to display in the list view
    list_display = ['username', 'email', 'is_staff', 'is_superuser']

admin.site.register(User, MyUserAdmin)