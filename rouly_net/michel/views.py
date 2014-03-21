from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import os

def error(request):
    return render(request, 'error.html', {
    },
    )

def home(request):
    return render(request, 'home.html', {
    },
    )

def work(request):
    return render(request, 'work.html', {
    },
    )

def research(request):
    return render(request, 'research.html', {
    },
    )

def community(request):
    return render(request, 'community.html', {
    },
    )

def contact(request):
    return render(request, 'contact.html', {
    },
    )
