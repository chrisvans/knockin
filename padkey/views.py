from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import Context, loader
from knockin import GeneratePasscode, AuthenticatePasscode
from models import Passcode, Diagnoser
from datetime import datetime


def log_passcode(passcode, success=False):
    log_passcode = Diagnoser(used_passcode=passcode)
    log_passcode.was_successful = success
    log_passcode.save()


def failure_counter(request):

    if request.user.is_authenticated():
        return True

    if 'failure_counter' in request.session:
        request.session['failure_counter'] += 1

    else:
        request.session['failure_counter'] = 1

    return False


def failure_blocker(request):

    if ('failure_counter' in request.session) and (request.session['failure_counter'] > 10):
        return True


def passcode(request, message='Enter Passcode'):

    if failure_blocker(request):
        return HttpResponseRedirect('http://www.bobzyeruncle.com/archives/debt-thumb.jpg')

    if request.method == 'POST':
        now = datetime.utcnow()
        passcode_attempt = request.POST['passcode']
        passcode_check = Passcode.objects.filter(is_active=True).filter(passcode=passcode_attempt)

        if passcode_check.exists():
            actual_passcode = passcode_check.get(passcode=passcode_attempt)
            timestamp_to_evaluate = actual_passcode.timestamp.replace(tzinfo=None)
            lockout_check = now - timestamp_to_evaluate

            if lockout_check.seconds < actual_passcode.lockout_time:
                log_passcode(passcode=actual_passcode.passcode, success=True)
                message = 'Proper Passcode'

            else:
                log_passcode(passcode=actual_passcode.passcode)
                message = 'Expired Passcode'
                actual_passcode.is_active = False
                actual_passcode.save()
                failure_counter(request)

        else:
            log_passcode(passcode=passcode_attempt)
            message = 'Bad Passcode'
            failure_counter(request)

    return render(request, 'index.html', {'message': message})


def generate_passcode(request, message=None):

    if request.user.is_authenticated():
        pass

    else:
        message = 'You must login to view this page!'
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        timeout = request.POST["timeout"]
        passcode = GeneratePasscode.generate_passcode()
        new_passcode = Passcode()
        new_passcode.passcode = passcode
        new_passcode.lockout_time = timeout
        new_passcode.save()
        message = Passcode.objects.get(passcode=new_passcode.passcode)

    passcode_logs = Diagnoser.objects.all()
    return render(request, 'admin.html', {'message': message,
                                          'passcode_logs': passcode_logs,
                                          })


def login_view(request, message=None):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if not user:
            message = 'Invalid Login!'
            return render(request, 'login.html', {'message': message})

        login(request, user)
        request.session['user'] = user
        request.user = user
        return HttpResponseRedirect(reverse('admin'))

    elif 'user' in request.session:
        return HttpResponseRedirect(reverse('admin'))

    return render(request, 'login.html', {'message': message})


def logout_view(request, message=None):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
