from django.urls import path
from projects.views import create_project, show_project, show_task

urlpatterns = [
    path("", show_project, name="list_projects"),
    path("<int:id>/", show_task, name="show_project"),
    path("create/", create_project, name="create_project"),
]
