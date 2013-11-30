from django.test import TestCase

class User(models.Model):
    email = models.TextField(unique=True)
