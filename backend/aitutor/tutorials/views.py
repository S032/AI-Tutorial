from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import markdown2

from rest_framework import viewsets
from .models import Language, Manual, Tutorial
from .serializers import LanguageSerializer

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
import json
import ai_module.ai_tutorial_ai as AI_module

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


def home(request):
    return render(request, 'tutorials/index.html')

def in_development(request):
    return render(request, 'tutorials/in_development.html')


def language_course(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    manuals = Manual.objects.filter(language=language)
    
    # Select the first tutorial automatically
    current_tutorial = None
    if manuals.exists():
        first_manual = manuals.first()
        first_topic = first_manual.topic_set.first()
        if first_topic:
            current_tutorial = first_topic.tutorial_set.first()
            
            # Convert tutorial content to HTML using markdown
            if current_tutorial:
                current_tutorial.content = markdown2.markdown(
                    current_tutorial.content, 
                    extras=['fenced-code-blocks', 'tables', 'highlight']
                )
    
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
        'id': tutorial_id,
        'name': tutorial.name,
        'content': html_content,
        'publication_date': tutorial.publication_date.strftime('%Y-%m-%d')
    })

def generate_code_problem_api(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)

    # Generate the code problem
    ai = AI_module.AITutorialGenerator()
    generated_problem = ai.generate_tutorial(tutorial.name, tutorial.content)

    request.session['code_problem_right_answer'] = generated_problem['practical_task_answer']['output']

    generated_problem['example_task']['code'] = markdown2.markdown(generated_problem['example_task']['code'], extras=['fenced-code-blocks', 'tables', 'highlight'])

    return JsonResponse(generated_problem)

def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")

@csrf_protect
@require_POST
def validate_solution_api(request, tutorial_id):
    import time
    time.sleep(2)

    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    
    # Parse the request body
    try:
        data = json.loads(request.body)
        user_solution = data.get('user_solution', '').strip()
    except json.JSONDecodeError:
        return JsonResponse({
            'is_correct': False,
            'error': 'Invalid JSON'
        }, status=400)
    
    # Retrieve the right answer from the session
    right_answer = request.session.get('code_problem_right_answer')
    
    # Compare solutions
    is_correct = user_solution == right_answer

    return JsonResponse({
        'is_correct': is_correct,
        'right_answer': right_answer
    })
