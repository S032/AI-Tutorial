from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'tutorials/indexbetter.html')


def tutorial(request, tutorial_id):
    return HttpResponse(f"Tutorial id {tutorial_id}")


def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")
