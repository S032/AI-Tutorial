from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path("", views.home, name="homepage"),
    path("api/", include(router.urls)),
    path("api/tutorials/<int:tutorial_id>/", views.tutorial_api, name="tutorial_api"),
    path("api/generate_problem/<int:tutorial_id>", views.generate_code_problem_api, name="generate_problem"),
    path("<int:language_id>/", views.language_course, name="language_course"),
    path("<int:tutorial_id>/givemecodeproblem/",
         views.givemecodeproblem, name="givemecodeproblem"),
    path("in_development/", views.in_development, name="in_development"),
    path('api/validate_solution/<int:tutorial_id>/', views.validate_solution_api, name='validate_solution_api'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
