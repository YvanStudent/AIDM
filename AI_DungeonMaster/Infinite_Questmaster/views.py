from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import openai

openai_api_key = 'sk-proj-tE9ZjEUH7mHYVBcHpKEWT3BlbkFJEvbRhvYRlRjso8jfF2Og'
openai.api_key = openai_api_key

def signuppage(request):
    """
    form = CreateUserFrom

    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    
    """
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created from ' + user)
            return redirect('login')
   

    context = {'form': form}
    return render(request, 'signup.html', context)

def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect.')
            return render(request, 'login.html', context)

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def account1(request):
    return render(request, 'account1.html')

def account2(request):
    return render(request, 'account2.html')

def account3(request):
    return render(request, 'account3.html')

def res_openai(message):
    response = openai.Completions.create(
        model = "text-davinci-003",
        prompt = message,
        max_token = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )

    print(response)

    #answer = response.choice[0].text.strip()
    #return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = res_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')