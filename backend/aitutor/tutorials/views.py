from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import markdown2

from rest_framework import viewsets
from .models import Language, Manual, Tutorial
from .serializers import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


def home(request):
    return render(request, 'tutorials/indexbetter.html')


def language(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    manuals = Manual.objects.filter(language=language)
    current_tutorial = None
    return render(request, 'tutorials/tutorial_page.html', {
        'language': language,
        'manuals': manuals,
        'current_tutorial': current_tutorial
    })


def tutorial(request, tutorial_id):
    return HttpResponse(f"Tutorial id {tutorial_id}")

def tutorial_api(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    html_content = markdown2.markdown(tutorial.content, extras=['fenced-code-blocks', 'tables', 'highlight'])
    return JsonResponse({
        'name': tutorial.name,
        'content': html_content,
        'publication_date': tutorial.publication_date.strftime('%Y-%m-%d')
    })


def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")
