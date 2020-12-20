from django.db import models



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