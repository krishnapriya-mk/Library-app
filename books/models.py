from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    authorname=models.CharField(max_length=255)
    def __str__(self):
        return self.authorname
class Book (models.Model):
    bookname=models.CharField(max_length=50,unique=True)
    brief_description=models.CharField(max_length=40,default="Really great book ")
    description=models.TextField(default="")
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)