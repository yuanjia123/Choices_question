from django.db import models
from django.contrib.auth.models import AbstractUser


class Grade(models.Model):
    g_name = models.CharField(max_length=200)

class User(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=200)
    g = models.ForeignKey(Grade, on_delete=True)

class Student(models.Model):
    sname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='imgs')

    def __str__(self):
        return self.sname



# 使用django自带的表   1、需要先继承AbstractUser   2、在setting当中设置#继承django自带的用户类  第二步AUTH_USER_MODEL = "users.User_k"
class UserProfile(AbstractUser):
    password= models.CharField(max_length=200,null=True)
    # class Meta:
        # db_table = "user_myself"