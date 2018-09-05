from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'UserModel'
