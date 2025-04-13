from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)


class Visit(models.Model):
    count = models.IntegerField(default=0)


