from django.contrib import admin
from .models import Blog

class Date_output(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Blog, Date_output)