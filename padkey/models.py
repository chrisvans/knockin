from django.db import models

class Passcode(models.Model):
    passcode = models.CharField(max_length=4, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    def __unicode__():
        return unicode(passcode) + " " + unicode(timestamp)
