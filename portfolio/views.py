from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def base(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/base.html', {'projects': projects})

def port(request, work_id):
    work = get_object_or_404(Project, pk = work_id)
    return render(request, 'portfolio/work.html', {'work': work})