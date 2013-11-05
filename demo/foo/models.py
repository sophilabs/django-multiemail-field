from django.db import models
from multiemailfield.fields import MultiEmailField


class Foo(models.Model):

    emails = MultiEmailField()
