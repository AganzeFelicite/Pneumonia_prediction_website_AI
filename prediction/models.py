from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10)
    test = models.CharField(max_length=10)
    age = models.IntegerField()
    
    def __str__(self):
        return self.user_id
    