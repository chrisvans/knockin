from django.db import models

class Passcode(models.Model):
    passcode = models.CharField(max_length=4, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    is_active = models.BooleanField(default=True)
    # Value expected to represent seconds
    lockout_time = models.IntegerField(default=900)

    def __unicode__(self):
        return "%s %s %s %s" % (self.passcode, self.timestamp, self.is_active, self.lockout_time)
