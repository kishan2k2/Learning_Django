from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"

def vote(request, question_id):
    # return HttpResponse('You are voting %s'% pk)
    question = get_object_or_404(Question, pk = question_id)
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