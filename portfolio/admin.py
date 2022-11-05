from django.contrib import admin
from .models import Project


class Date_output(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Project, Date_output)