from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.urlresolvers import reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.template import Context, loader
from knockin import GeneratePasscode, AuthenticatePasscode
from models import Passcode


def passcode(request):
    message = 'This is where the user will enter in the passcode.'

    if request.method == 'POST':
        passcode_attempt = request.POST['passcode']
        pass

    return render(request, 'index.html', { 'message' : message })

def generate_passcode(request):
    # Verify that valid user is logged in
    message = 'Nothing happened'

    if request.method == 'POST':
        passcode = GeneratePasscode.generate_passcode()
        new_passcode = Passcode()
        new_passcode.passcode = passcode
        new_passcode.save()
        message = Passcode.objects.get(passcode=new_passcode.passcode)

    return render(request, 'admin.html', { 'message' : message })