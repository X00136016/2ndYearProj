from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.articles, name='articles'),
    path('article/<article>', views.article, name='article'),
    path('jobs', views.jobs, name='jobs'),
]