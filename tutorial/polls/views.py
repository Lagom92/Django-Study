from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


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
    question = get_object_or_404(Question, id=id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except:
        context = {
            'question': question,
            'error_message': "선택을 하지 않았습니다."
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
