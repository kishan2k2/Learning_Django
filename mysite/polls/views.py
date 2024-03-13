from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import F 
from django.urls import reverse
# Create your first views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
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
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/result.html", {"question":question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Phir se question ko display karenge taaki sahi option ko choose karle.
        return render(
            request,
            'polls/details.html',
            {
                "question":question,
                "error_message":"You didn't choose any option",
            }
        )
    else:
        selected_choice.votes = F('votes') + 1 # I don't know if the votes in the database in changed or the selected choice is updated by extracting the value from the votes
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id, )))