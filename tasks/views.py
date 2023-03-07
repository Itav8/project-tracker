from django.shortcuts import redirect, render
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required(redirect_field_name="user_login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.assignee = request.user
            task.save()
            return redirect("show_project", id=task.project.id)
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)


@login_required(redirect_field_name="user_login")
def list_task(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/list_task.html", context)
