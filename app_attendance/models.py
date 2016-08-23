from django.db import models

class Person(models.Model):
    id   = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=14)

class Dedada(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    date   = models.DateTimeField(blank = False)
