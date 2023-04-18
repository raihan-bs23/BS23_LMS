from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, time, datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def Home(request):
    return render(request, 'pages/home.html')
