from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import QueryDict
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.utils import unittest
from django.utils.importlib import import_module
from padkey.views import passcode, generate_passcode, login_view, logout_view
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
        self.user = User()
        self.user.username = 'Chris'
        self.user.password = 'bagel'
        self.user.set_password('bagel')
        self.user.save()

    def tearDown(self):
        all_passcodes = Passcode.objects.all()
        for passcode in all_passcodes:
            passcode.delete()
        all_users = User.objects.all()
        for user in all_users:
            user.delete()

    def generate_passcodes(self):
        passcode = Passcode()
        passcode.passcode = '0232'
        passcode.save()
        expired_passcode = Passcode()
        expired_passcode.passcode = '0101'
        expired_passcode.lockout_time = -1
        expired_passcode.save()

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
        self.generate_passcodes()
        request = self.factory.post('/', {'passcode': '0101'})
        request.session = self.session
        request.user = self.anon_user
        response = passcode(request)
        self.assertEquals(response.status_code, 200)
        check_expired_passcode = Passcode.objects.get(passcode='0101')
        self.assertEquals(check_expired_passcode.is_active, False)        

    def test_that_generate_passcode_view_GET_with_anon_user_returns_302(self):
        request = self.factory.get('/admin/')
        request.session = self.session
        request.user = self.anon_user
        response = generate_passcode(request)
        response.client = self.client
        self.assertEquals(response.status_code, 302)

    def test_that_generate_passcode_view_POST_with_anon_user_does_not_generate_passcode_and_returns_302(self):
        request = self.factory.post('/admin/', {'timeout': '15'})
        request.session = self.session
        request.user = self.anon_user
        response = generate_passcode(request)
        response.client = self.client
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Passcode.objects.all().exists(), False)

    def test_that_generate_passcode_view_GET_with_user_returns_200(self):
        request = self.factory.get('/admin/')
        request.session = self.session
        request.user = self.user
        response = generate_passcode(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)        

    def test_that_generate_passcode_view_POST_with_user_generates_passcode_and_returns_200(self):
        request = self.factory.post('/admin/', {'timeout': '15'})
        request.session = self.session
        request.user = self.user
        response = generate_passcode(request)
        response.client = self.client
        self.assertEquals(response.status_code, 200)  

    def test_that_logout_view_logs_user_out_if_user_and_returns_302(self):
        request = self.factory.get('/logout/')
        request.session = self.session
        request.user = self.user
        response = logout_view(request)
        response.client = self.client
        self.assertEquals(response.status_code, 302)
        self.assertNotIn('user', self.session)

