#!/usr/bin/env python

import unittest

from padkey.knockin import GeneratePasscode, AuthenticatePasscode
from padkey.models import Passcode

GOOD_TESTCODE = '0000'
BAD_TESTCODE = '9999'

class TestKnockin(unittest.TestCase):

    def setUp(self):
        self.test_passcode = Passcode()
        self.test_passcode.passcode = GOOD_TESTCODE
        self.test_passcode.save()

    def tearDown(self):
        for passcode in Passcode.objects.all():
            passcode.delete()

    def test_is_unique(self):
        self.assertFalse(GeneratePasscode.is_unique(self.test_passcode.passcode))
        self.assertTrue(GeneratePasscode.is_unique(BAD_TESTCODE))

    def test_successful_generate(self):
        dump = Passcode.objects.all()
        self.assertEquals(len(dump), 1, dump)

    def test_authenticate_success(self):
        self.assertTrue(AuthenticatePasscode.authenticate(self.test_passcode.passcode))

    def test_authenticate_fail(self):
        self.assertFalse(AuthenticatePasscode.authenticate(BAD_TESTCODE))

if __name__ == "__main__":
    unittest.main()
