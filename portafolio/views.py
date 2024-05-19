from django.shortcuts import render, get_object_or_404
from.models import Project

def home(request):
        projects = Project.objects.all().order_by('id')
        print(type(projects))
        return render(request, 'home.html', {'projects': projects})

def project_detail(request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        print(type(project))
        return render(request, "project_detail.html", {"project":project})