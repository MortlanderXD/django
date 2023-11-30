from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/members/login/")
def index(request):
    latest_question_list = Question.objects.all
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)

    except Question.DoesNotExist:
        return render(request,"error.html")

    return render(request, "detail.html",{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,"detail.html",{"question": question,
                "error_message": "Choisis je te dis.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    if question.id +1 <= Question.objects.count() :
        return HttpResponseRedirect(reverse("members:detail", args=(question.id+1,)))
    else:
        return HttpResponse("Félicitations ! Vous avez tous rempli !")

class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"

def login_view(request):
    #if request.user.is_authenticated:
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/members')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponse("Logout Completed ! ")