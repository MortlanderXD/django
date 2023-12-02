from django.shortcuts import render, HttpResponse , redirect , HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login , logout 
# Create your views here.
from django.urls import reverse


def index(request):
    isConnected = request.user.is_authenticated
    context = {"isConnected": isConnected}
    return render(request,'tricount/index.html',context)


def loginView(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            isConnected = request.user.is_authenticated
            context = {"isConnected": isConnected}
            return redirect('/tricount')
    return render(request, 'tricount/login.html', {'form': form})


def logout_view(request):
    logout(request)
    isConnected = request.user.is_authenticated
    context = {"isConnected": isConnected}
    return HttpResponseRedirect('/tricount')