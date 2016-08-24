from django.db import models

class Person(models.Model):
    id   = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=14)

class Fingerprint(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    moment = models.DateTimeField(blank = False)

class WorkedTime(models.Model):
    start  = models.ForeignKey(Fingerprint, 
                               on_delete    = models.CASCADE,
                               blank        = False,
                               related_name = "workedtime_start")

    finish = models.ForeignKey(Fingerprint, 
                               on_delete    = models.CASCADE,
                               blank        = True,
                               related_name = "workedtime_finish")
