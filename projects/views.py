from django.shortcuts import render
from projects.models import Project


# Create your views here.
def show_project(request):
    projects = Project.objects.all()
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list_project.html", context)
