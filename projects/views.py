from django.shortcuts import redirect, render
from projects.forms import ProjectForm
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(redirect_field_name="user_login")
def show_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list_project.html", context)


@login_required(redirect_field_name="user_login")
def show_task(request, id):
    tasks = Task.objects.filter(project=id)
    context = {"task_list": tasks, "project": Project.objects.get(id=id)}

    return render(request, "projects/detail_project.html", context)


@login_required(redirect_field_name="user_login")
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)
