from django.shortcuts import render
from .models import Job

from django.views.generic import TemplateView

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

    
class HomePageView(TemplateView):
    template_name = 'jobs/home.html'