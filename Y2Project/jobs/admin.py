from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Job
from .models import Category
from .models import Company
# Register your models here.

admin.site.register(Job, MarkdownxModelAdmin)
admin.site.register(Category, MarkdownxModelAdmin)
admin.site.register(Company, MarkdownxModelAdmin)