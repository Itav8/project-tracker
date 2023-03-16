from django.shortcuts import redirect, render
from projects.models import Project
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required(redirect_field_name="user_login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.save()

            return redirect("show_project", id=task.project.id)
    else:
        form = TaskForm()

    form.fields["project"].queryset = Project.objects.filter(
        owner=request.user.id
    )

    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)


@login_required(redirect_field_name="user_login")
def list_task(request):
    tasks = Task.objects.filter(assignee=request.user)

    if request.method == "GET":
            query = request.GET.get("query", "")

            if query:
                tasks = Task.objects.filter(
                    name__icontains=query, assignee=request.user
                )

    context = {
        "task_list": tasks,
    }

    return render(request, "tasks/list_task.html", context)
