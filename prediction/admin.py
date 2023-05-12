from django.contrib import admin
from .models import Users


class User(admin.ModelAdmin):
    list_display = ('user_id', 'gender', 'test', 'age')

admin.site.register(Users, User)




# Register your models here.
