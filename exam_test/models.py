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