from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.



def index(request):
    latest_question_list = Question.objects.all
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)


# def detail(request, question_id):
#     try:
#         quest = Question.objects.get(id=question_id)
#         questt = quest.question_text
#         response_text = f'You are looking "{questt}" at question {question_id}.'
#         return HttpResponse(response_text)
    
#     except Question.DoesNotExist:
#         return render(request,"error.html")

def detail(request, question_id):

    try:
        question = Question.objects.get(id=question_id)
        text = question.question_text
        

    except Question.DoesNotExist:
        return render(request,"error.html")

    return render(request, "detail.html", {"question": question , "text" : text})



def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
