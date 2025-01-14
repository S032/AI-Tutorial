from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path("", views.home, name="homepage"),
    path("api/", include(router.urls)),
    path("api/tutorials/<int:tutorial_id>/", views.tutorial_api, name="tutorial_api"),
    path("<int:language_id>/", views.language, name="language"),
    path("<int:tutorial_id>/givemecodeproblem/",
         views.givemecodeproblem, name="givemecodeproblem")
]
