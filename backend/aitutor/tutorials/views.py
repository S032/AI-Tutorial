from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


def home(request):
    return render(request, 'tutorials/indexbetter.html')


def tutorial(request, tutorial_id):
    return HttpResponse(f"Tutorial id {tutorial_id}")


def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")
