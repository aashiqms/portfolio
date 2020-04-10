import pdb

from django.shortcuts import render
from .models import Job
from jobs.forms import NewUserForm
from .forms import FeedbackForm
from django.http import HttpResponse
from django.http import Http404
import pdb


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


# Feedback #

def index(request):
    return render(request, 'jobs/home.html')


def users_function(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # to save data to database and commitm it to database
            return index(request)
        else:
            print('ERROR')

    return render(request, 'jobs/users.html', {'form_key': form})


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'jobs/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'jobs/feedback.html', {'form': form})


def details(request, id):
    jobs = Job.objects.get(id=id)
    try:
        jobs = Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise Http404("Work doesn't exist")
    return render(request, 'jobs/details.html', {'jobs': jobs})


