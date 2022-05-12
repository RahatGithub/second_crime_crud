from django.shortcuts import render
# from .models import Case
# from accounts.models import Reporter
from django.contrib.auth.models import User, auth
from random import randint
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def reportCrime(request):
    pass


def dashboard(request, username):
    pass