from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Card(models.Model):
    no = models.CharField(max_length=4)
    status = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    motive = models.CharField(max_length=200)
    issuance_years = models.CharField(max_length=20)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
