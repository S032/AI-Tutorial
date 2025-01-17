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
        'id': tutorial_id,
        'name': tutorial.name,
        'content': html_content,
        'publication_date': tutorial.publication_date.strftime('%Y-%m-%d')
    })

def generate_code_problem_api(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    module1 = """
**Задача:** Написать функцию, которая вычисляет площадь прямоугольника.
**Код:**

```cpp
#include <iostream>

using namespace std;

double calculateArea(double length, double width) {
  return length * width;
}

int main() {
  double length, width;
  cout << "Введите длину прямоугольника: ";
  cin >> length;
  cout << "Введите ширину прямоугольника: ";
  cin >> width;

  double area = calculateArea(length, width);
  cout << "Площадь прямоугольника: " << area << endl;
  return 0;
}
```

**Ввод:**

```
Введите длину прямоугольника: 5
Введите ширину прямоугольника: 10
```

**Вывод:**

```
Площадь прямоугольника: 50
```
"""
    module2 = "Not exists"
    module3 = "Not exists"

    html_module_1 = markdown2.markdown(module1, extras=['fenced-code-blocks', 'tables', 'highlight'])
    html_module_2 = markdown2.markdown(module2, extras=['fenced-code-blocks', 'tables', 'highlight'])
    html_module_3 = markdown2.markdown(module3, extras=['fenced-code-blocks', 'tables', 'highlight'])
    import time
    time.sleep(5)

    example_task = {
        "task_description" : "Write a function that calculates the area of a rectangle.",
        "example_code": markdown2.markdown("""
```cpp
#include <iostream>

using namespace std;

double calculateArea(double length, double width) {
  return length * width;
}

int main() {
  double length, width;
  cout << "Введите длину прямоугольника: ";
  cin >> length;
  cout << "Введите ширину прямоугольника: ";
  cin >> width;

  double area = calculateArea(length, width);
  cout << "Площадь прямоугольника: " << area << endl;
  return 0;
}
```
""", extras=['fenced-code-blocks', 'tables', 'highlight']),
        "example_input_and_output": markdown2.markdown("""
Ввод:
```
Введите длину прямоугольника: 5
Введите ширину прямоугольника: 10
```
Вывод:
```
Площадь прямоугольника: 50
```
""", extras=['fenced-code-blocks', 'tables', 'highlight'])
    }

    practical_task = {
        "task_description" : markdown2.markdown("Write a function that calculates the area of a rectangle.", extras=['fenced-code-blocks', 'tables', 'highlight']),
        "input_output_requirements": markdown2.markdown("""
Ввод:
```
Введите длину прямоугольника: 5
Введите ширину прямоугольника: 10
```
Вывод:
```
Площадь прямоугольника: 50
```
""", extras=['fenced-code-blocks', 'tables', 'highlight'])
    }

    input_validation = {
        "input": markdown2.markdown("""
Ввод:
```
Введите длину прямоугольника: 5
Введите ширину прямоугольника: 10
```
""", extras=['fenced-code-blocks', 'tables', 'highlight'])
    }

    return JsonResponse({
        "example_task": example_task,
        "practical_task": practical_task,
        "input_validation": input_validation,
        "right_answer": "17"
    })
    


def givemecodeproblem(request, tutorial_id):
    return HttpResponse(f"problem for tutorial which id is {tutorial_id}")
