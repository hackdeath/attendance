from django.db import models

class Person(models.Model):
    id   = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=14)

    def __str__(self):
      return "{0} - {1}".format(self.id, self.name)

class Fingerprint(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    moment = models.DateTimeField(blank = False)

    def __str__(self):
      return "{0} - {1}".format(self.person, self.moment)

class WorkedTime(models.Model):
    start  = models.ForeignKey(Fingerprint, 
                               on_delete    = models.CASCADE,
                               null        = False,
                               related_name = "workedtime_start")

    finish = models.ForeignKey(Fingerprint, 
                               on_delete    = models.CASCADE,
                               null        = True,
                               related_name = "workedtime_finish")

    def __str__(self):
      return "Start: {0} Finish: {1}".format(self.start, self.finish)
