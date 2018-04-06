from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
    template = loader.get_template('jobs/jobs.html')
    return HttpResponse(template.render(None, request))