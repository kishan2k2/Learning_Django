from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("Date published")#Lets see if it is an keyword or just a string argument.
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days = 1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)# What does it means.
    choice_text =  models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
