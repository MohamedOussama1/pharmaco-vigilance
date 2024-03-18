from django.urls import path
from . import views


urlpatterns = [
    path("patient", views.patients, name="patients"),
]