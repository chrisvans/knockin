from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import QueryDict
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.utils import unittest
from django.utils.importlib import import_module
from padkey.views import passcode, generate_passcode
from padkey.models import Passcode
import datetime


class GenericViewTests(TestCase):

    def setUp(self):
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client = Client()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
        self.factory = RequestFactory()
        self.anon_user = AnonymousUser()
        passcode = Passcode()
        passcode.passcode = '0232'
        passcode.save()
        expired_passcode = Passcode()
        expired_passcode.passcode = '0101'
        expired_passcode.lockout_time = -1
        expired_passcode.save()

    def tearDown(self):
        all_passcodes = Passcode.objects.all()
        for passcode in all_passcodes:
            passcode.delete()

    def test_that_passcode_view_GET_returns_200(self):
        request = self.factory.get('/')
        request.session = self.session
        request.user = self.anon_user
        response = passcode(request)
        self.assertEquals(response.status_code, 200)

    def test_that_passcode_view_POST_good_passcode_opens_door_with_200(self):
        request = self.factory.post('/', {'passcode': '0232'})
        request.session = self.session
        request.user = self.anon_user
        response = passcode(request)
        self.assertEquals(response.status_code, 200)

    def test_that_passcode_view_POST_bad_passcode_fails_adds_to_anon_user_count_session_with_200(self):
        request = self.factory.post('/', {'passcode': 'cheesecake'})
        request.session = self.session
        request.user = self.anon_user
        response = passcode(request)
        self.assertEquals(response.status_code, 200)

    def test_that_passcode_view_POST_expired_passcode_fails_and_sets_is_active_to_false_with_200(self):
        request = self.factory.post('/', {'passcode': '0101'})
        request.session = self.session
        request.user = self.anon_user
        response = passcode(request)
        self.assertEquals(response.status_code, 200)
        check_expired_passcode = Passcode.objects.get(passcode='0101')
        self.assertEquals(check_expired_passcode.is_active, False)        

    def test_that_generate_passcode_view_GET_returns_200(self):
        request = self.factory.get('/admin/')
        request.session = self.session
        request.user = self.anon_user
        response = generate_passcode(request)
        self.assertEquals(response.status_code, 200)

    def test_that_generate_passcode_view_POST_generates_passcode_and_returns_200(self):
        request = self.factory.post('/admin/')
        request.session = self.session
        request.user = self.anon_user
        response = generate_passcode(request)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Passcode.objects.all().exists(), True)


