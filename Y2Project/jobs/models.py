from django.db import models
from datetime import date
from markdownx.models import MarkdownxField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    type = models.IntegerField()
    description = MarkdownxField(help_text="Markdown Enabled")


    class Meta():
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=30)
    description = MarkdownxField(help_text="Markdown Enabled")

    class Meta():
        verbose_name_plural = "Companies"
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=30)
    content = MarkdownxField(help_text="Markdown Enabled")
    date_posted = models.DateField('Date Posted', default=date.today)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
