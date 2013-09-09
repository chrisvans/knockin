#!/usr/bin/env python

import random
import string
import sys
from models import Passcode
from datetime import datetime

def KnockinException(Exception):
    pass


class GeneratePasscode():
    @classmethod
    def is_unique(cls, code):
        check_for_passcode = Passcode.objects.filter(passcode=code)
        if check_for_passcode.exists():
            return False
        else:
            return True
    
    @classmethod
    def generate_passcode(cls):
        now = datetime.utcnow()
        # Only generate a 4-digit passcode
        unique = False
        while not unique:
            code = ''.join(random.choice(string.digits) for x in range(4))
            unique = cls.is_unique(code)

        return (code, now)


class AuthenticatePasscode():
    @classmethod
    def authenticate(cls, code):
        passcode_check = Passcode.objects.filter(is_active=True).filter(passcode=code)
        # check for active passcode
        if passcode_check.exists():
            return True
        else:
            return False


def run():
    passcode, time = GeneratePasscode.generate_passcode()
    print "generated passcode %s at %s" % (passcode, time)
