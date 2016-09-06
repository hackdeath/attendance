from django.db import models

class Person(models.Model):
    id   = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 14)

    def __str__(self):
      return "{0} - {1}".format(self.id, self.name)

class Date(models.Model):
    date_fingerprint = models.DateField(blank = True, null = True)

    def __str__(self):
      return "{0}".format(self.date_fingerprint)

class WorkedTime(models.Model):
    person   = models.ForeignKey(Person, on_delete = models.CASCADE, null = True, related_name="work_times", related_query_name="work_times")
    date     = models.ForeignKey(Date,   on_delete = models.CASCADE, null = True, related_name="work_times", related_query_name="work_times")
    
    initial  = models.TimeField(null = False)
    final    = models.TimeField(null = True)

    def __str__(self):
        return "Person: {0} Date: {1} Initial: {2} Final: {3}".format(self.person, self.date, self.initial, self.final)

    def calc_timedelta():
        try:
            return final - initial
        except AttibuteError:
            return timedelta(seconds=0)
