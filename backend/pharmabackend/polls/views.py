from django.http import HttpResponse
import datetime
from polls.utils import *
from polls.models import *


def index(request):
    connect_to_db("pharmaco")

    choice_1 = Choice(choice_text="Good")
    choice_2 = Choice(choice_text="Bad")

    question_1 = Question(question_text="How are you?",
                          pub_date=datetime.datetime.now(),
                          choices=[choice_1, choice_2])

    question_2 = Question(question_text="How are you?",
                          pub_date=datetime.datetime.now(),
                          choices=[choice_1, choice_2])

    question_1.save()
    question_2.save()

    return HttpResponse(Question.objects())


