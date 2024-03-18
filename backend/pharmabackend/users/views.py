from django.http import HttpResponse
import datetime
from users.utils import *
from users.models import *


def get_users(request):
    connect_to_db("pharmaco")
    user1 = Patient(first_name="John", last_name="Doe", email="a@gmail.com", age=20, national_identifier_code="FN203238", phone_number="0238238823")
    user1.save()

    return HttpResponse(User.objects())

