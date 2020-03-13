from django.shortcuts import render, get_object_or_404
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
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, id):
    response = "Results of Question"
    return HttpResponse(response)

def vote(request, id):
    return HttpResponse(f"Vote {id}번 question")