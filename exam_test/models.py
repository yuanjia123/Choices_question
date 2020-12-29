from django.db import models

# Create your models here.

class Choice(models.Model):

    choice_text = models.CharField(max_length=2000)
    a = models.CharField(max_length=2000)
    b = models.CharField(max_length=2000)
    c = models.CharField(max_length=2000)
    d = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)
    think = models.CharField(max_length=2000)
    #
    # def __str__(self):
    #     return self.answer
class User_1(models.Model):
    username = models.CharField(max_length=50)
    gender = models.BooleanField()

class Data_weather(models.Model):

    city = models.CharField(max_length=50,null=False)
    ymd = models.CharField(max_length=50,null=False)
    tianqi = models.CharField(max_length=50,null=False)
    bWendu = models.CharField(max_length=50,null=False)
    yWendu = models.CharField(max_length=50,null=False)
    fenli = models.CharField(max_length=50,null=False)
    fenxiang = models.CharField(max_length=50,null=False)
    yer = models.CharField(max_length=50,null=False)
    month = models.CharField(max_length=50,null=False)
