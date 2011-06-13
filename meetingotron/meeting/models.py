from django.db import models
import datetime

# Create your models here.
class Meeting(models.Model):

    title = models.CharField(max_length = 255, null=False, blank=False)
    purpose = models.TextField(max_length = 300, null=True, blank=True)
    date_time_started = models.DateTimeField(auto_now_add = True)
    length_in_minutes = models.IntegerField()
    etherpad_url = models.URLField(max_length=200, null=True, blank=True)

    def expired(self):
        return datetime.datetime.now() > (self.date_time_started + datetime.timedelta(0,self.length_in_minutes * 60))