from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    homePage_text = "This is home page where you can find tutorials"
    return HttpResponse(homePage_text)


def tutorial(request, tutorial_id):
    return HttpResponse(f"Tutorial id {tutorial_id}")


def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")
