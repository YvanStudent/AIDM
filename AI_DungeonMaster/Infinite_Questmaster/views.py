from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def index(request):
    # Determine which template to render based on the request
    template_name = 'home.html'  # Default template is home.html

    if request.path == '/about/':
        template_name = 'about.html'
    elif request.path == '/login/':
        template_name = 'login.html'
    elif request.path == '/logout/':
        template_name = 'logout.html'

    return render(request, template_name)

def about(request):
    return render(request, 'about.html')

def login2(request):
    return render(request, 'login2.html')

def signup(request):
    return render(request, 'signup.html')

def feedback(request):
    return render(request, 'feedback.html')

def register(request):
    # Add your registration logic here
    return HttpResponse("This is the registration page")