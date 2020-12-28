from django.db import models

class Person(models.Model):
   name = models.CharField(max_length=50)
   gender = models.CharField(max_length=50)
   age= models.IntegerField(default=5)

def __str__(self):
   return self.name


class Comment(models.Model):
   comment = models.TextField(max_length=200)
   news = models.TextField()


def __str__(self):
   return self.comment