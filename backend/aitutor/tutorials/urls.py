from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("<int:tutorial_id>/", views.tutorial, name="tutorial"),
    path("<int:tutorial_id>/givemecodeproblem/",
         views.givemecodeproblem, name="givemecodeproblem")
]
