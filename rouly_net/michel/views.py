from django.shortcuts import render

def error_404(request):
    return render(request, '404.html', {
    },
    )

def error_500(request):
    return render(request, '500.html', {
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
