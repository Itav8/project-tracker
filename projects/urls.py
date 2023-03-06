from django.urls import path

from projects.views import show_project

urlpatterns = [
    path("", show_project, name="list_projects"),
]
