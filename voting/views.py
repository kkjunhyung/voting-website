from django.shortcuts import render, get_object_or_404, redirect
from .models import Project

def project_list(request):
    projects = Project.objects.all().order_by('-votes')
    return render(request, 'project_list.html', {'projects': projects})

def vote(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.votes += 1
    project.save()
    return redirect('/')