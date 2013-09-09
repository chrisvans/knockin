from django.db import models

class Passcode(models.Model):
    passcode = models.CharField(max_length=4, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.passcode) + " " + unicode(self.timestamp)
