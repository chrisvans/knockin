from django.db import models
from django.utils.timezone import activate, localtime


class Passcode(models.Model):
    passcode = models.CharField(max_length=4, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    is_active = models.BooleanField(default=True)
    # Value expected to represent seconds
    lockout_time = models.IntegerField(default=900)

    def __unicode__(self):
        return "Passcode '%s' created and will expire in '%s' minutes." % (self.passcode, self.lockout_time)

    def get_information(self):
        return "%s %s %s %s" % (self.passcode, self.timestamp, self.is_active, self.lockout_time)


class Diagnoser(models.Model):
    used_passcode = models.CharField(max_length=4, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    def __unicode__(self):
        return "Passcode '%s'" % (self.used_passcode)

    def get_timestamp(self):
        server_time = localtime(self.timestamp)

        activate(server_time.tzinfo)
        return server_time
