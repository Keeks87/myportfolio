# projects/views.py

# Import render and Project Model
from django.shortcuts import render
from .models import Project


def project_list(request):
    """View function to display a list of projects."""
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, pk):
    """View function to display a single project."""
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
