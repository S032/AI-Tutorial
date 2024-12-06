from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path("", views.home, name="homepage"),
    path("api/", include(router.urls)),
    path("<int:tutorial_id>/", views.tutorial, name="tutorial"),
    path("<int:tutorial_id>/givemecodeproblem/",
         views.givemecodeproblem, name="givemecodeproblem")
]
