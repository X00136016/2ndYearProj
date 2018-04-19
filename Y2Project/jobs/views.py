from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Job
from markdownx.utils import markdownify

# Create your views here.

def index(request):
    template = loader.get_template('jobs/index.html')
    return HttpResponse(template.render(None, request))

def articles(request):
    template = loader.get_template('jobs/articles.html')
    return HttpResponse(template.render(None, request))

def article(request, article):
    template = loader.get_template('jobs/article.html')
    return HttpResponse(template.render(None, request))

def jobs(request):
    jobs = Job.objects.order_by('date_posted')
    template = loader.get_template('jobs/jobs.html')

    context = {
        'jobs': jobs
    }
    return HttpResponse(template.render(context, request))

def job(request, job_slug):
    job = get_object_or_404(Job, slug=job_slug)
    job.content = markdownify(job.content)
    return render(request, 'jobs/job.html', {'job': job})