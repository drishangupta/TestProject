from django.urls import path
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from . import views

app_name="polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>",views.detail,name="detail"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote")
]