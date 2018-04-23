from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.articles, name='articles'),
    path('article/<article>', views.article, name='article'),
    path('jobs', views.jobs, name='jobs'),
    path('job/<job_slug>', views.job, name='job_detail'),
    path('category/<category_slug>', views.category, name='category_view')
]