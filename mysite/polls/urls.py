from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    # To view the index of the website.
    path("", views.IndexView.as_view(), name='index'),
    # To view the question detail i.e. /polls/5
    path("specifies/<int:pk>/", views.DetailView.as_view() , name = 'details'),
    # To view the result.
    # /polls/question_id/result
    path('<int:pk>/result', views.ResultsView.as_view(), name = 'result'),
    # To view the vote.
    # /polls/question_id/vote
    path('<int:question_id>/vote', views.vote, name = 'vote'),
]