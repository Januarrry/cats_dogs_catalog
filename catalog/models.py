from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

class Dog(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)


class Feedback(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date_sent = models.DateTimeField("date sent")
