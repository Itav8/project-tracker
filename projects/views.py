from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(redirect_field_name="user_login")
def show_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list_project.html", context)
