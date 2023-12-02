from django.shortcuts import render, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
        
    return render(request,'tricount/index.html')


def loginView(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request, "tricount/index.html")
    return render(request, 'tricount/login.html', {'form': form})