from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your first views here.
from django.http import HttpResponse, Http404
from .models import Question, Choice
def index(request):
    # return HttpResponse('hello')
    latest_question = Question.objects.order_by('-pub_date')[:5]
    # output = '<br>'.join([q.question_text for q in latest_question])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question':latest_question
    }
    return render(request, 'polls/index.html', context)
    return HttpResponse(template.render(context, request))
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question':question})
    # return HttpResponse("You are viewing question id %s" %(question_id))
def result(request, question_id):
    return HttpResponse('You are viewing result of %s'%question_id)
def vote(request, question_id):
    return HttpResponse('You are voting %s'% question_id)