# Create your views here.

from django.views.generic import ListView
from .models import Job, Restaurant

class JobListView(ListView):
    model = Job
