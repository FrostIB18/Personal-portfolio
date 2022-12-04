from django.contrib import admin
from .models import Blog

#shows DateTimeField in admin
class Date_output(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Blog, Date_output)