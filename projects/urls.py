from django.urls import path

from projects.views import show_project, show_task

urlpatterns = [
    path("", show_project, name="list_projects"),
    path("<int:id>/", show_task, name="show_project"),
]
