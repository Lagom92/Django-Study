from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    res = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, id):
    return HttpResponse(f"{id}번 Question")

def results(request, id):
    response = "Results of Question"
    return HttpResponse(response)

def vote(request, id):
    return HttpResponse(f"Vote {id}번 question")