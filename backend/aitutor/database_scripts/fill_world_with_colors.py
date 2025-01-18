import os
import sys
import django
from datetime import date

# Добавляем путь к проекту
sys.path.append('/home/nadgox/Public/PublicProjects/Python/AI-Tutorial/backend/aitutor')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aitutor.settings')

# Инициализируем Django
django.setup()

from tutorials.models import Language, Manual, Topic, Tutorial, ColorScheme

def create_educational_content():
    # Очищаем существующие данные
    Tutorial.objects.all().delete()
    Topic.objects.all().delete()
    Manual.objects.all().delete()

    # Словарь с учебными материалами
    language_contents = {
        'Python': {
            'manuals': [
                {
                    'name': 'Основы Python',
                    'topics': [
                        {
                            'name': 'Введение в Python',
                            'tutorials': [
                                {
                                    'name': 'Первая программа',
                                    'content': '''
# Основы создания программы на Python

## Что такое Python?
Python - это высокоуровневый язык программирования, известный своей простотой и читаемостью. 
Он идеален для начинающих программистов и профессионалов.

## Установка Python
1. Скачайте дистрибутив с официального сайта python.org
2. Установите, отметив галочку "Add Python to PATH"
3. Проверьте установку командой `python --version`

## Первая программа
```python
# Классический пример "Hello, World!"
print("Привет, мир!")

# Переменные и типы данных
name = "Программист"
age = 25
is_student = True

# Форматированный вывод
print(f"Меня зовут {name}, мне {age} лет")

# Простые математические операции
x = 10
y = 5
print(f"Сумма: {x + y}")
print(f"Умножение: {x * y}")
```

## Управляющие конструкции
```python
# Условный оператор
if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вам еще рано")

# Цикл for
fruits = ["яблоко", "банан", "апельсин"]
for fruit in fruits:
    print(f"Мне нравится {fruit}")
```

## Функции
```python
def greet(name):
    """Функция приветствия"""
    return f"Привет, {name}!"

# Вызов функции
message = greet("Программист")
print(message)
```

## Что дальше?
- Изучите официальную документацию Python
- Практикуйтесь каждый день
- Решайте алгоритмические задачи
'''
                                },
                                {
                                    'name': 'Структуры данных в Python',
                                    'content': '''
# Структуры данных в Python

## Списки
```python
# Создание и базовые операции
fruits = ["яблоко", "банан", "апельсин"]

# Добавление элементов
fruits.append("груша")
fruits.insert(1, "манго")

# Удаление элементов
fruits.remove("банан")
last_fruit = fruits.pop()

# Срезы и операции
print(fruits[0:2])  # Первые два элемента
print(len(fruits))  # Длина списка

# Списковые включения
squared = [x**2 for x in range(1, 6)]
print(squared)  # [1, 4, 9, 16, 25]
```

## Словари
```python
# Создание словаря
student = {
    "name": "Иван",
    "age": 25,
    "courses": ["Python", "Алгоритмы"]
}

# Доступ к элементам
print(student["name"])
print(student.get("email", "Не указан"))

# Изменение и добавление
student["email"] = "ivan@example.com"
student["age"] += 1

# Перебор словаря
for key, value in student.items():
    print(f"{key}: {value}")
```

## Кортежи и Множества
```python
# Кортеж (неизменяемый список)
coordinates = (10, 20)
x, y = coordinates

# Множество (уникальные элементы)
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # {1, 2, 3}

# Операции с множествами
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
```
'''
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        'C++': {
            'manuals': [
                {
                    'name': 'Основы C++',
                    'topics': [
                        {
                            'name': 'Введение в C++',
                            'tutorials': [
                                {
                                    'name': 'Компиляция и основы синтаксиса',
                                    'content': '''
# Введение в C++: Компиляция и основы синтаксиса

## Что такое C++?
C++ - мощный язык программирования общего назначения, расширение языка C. 
Используется для системного программирования, разработки игр и высокопроизводительных приложений.

## Установка компилятора
1. GCC (Linux): `sudo apt-get install g++`
2. MinGW (Windows)
3. Xcode (MacOS)

## Первая программа
```cpp
#include <iostream>
using namespace std;

int main() {
    // Вывод на экран
    cout << "Привет, мир!" << endl;
    
    // Переменные и типы данных
    int age = 25;
    double height = 1.75;
    char grade = 'A';
    bool is_student = true;
    
    // Форматированный вывод
    cout << "Возраст: " << age << endl;
    cout << "Рост: " << height << " м" << endl;
}
```

## Компиляция программы
```bash
# Компиляция
g++ -o hello hello.cpp

# Запуск
./hello
```

## Управляющие конструкции
```cpp
#include <iostream>
using namespace std;

int main() {
    // Условный оператор
    int x = 10;
    if (x > 5) {
        cout << "x больше 5" << endl;
    } else {
        cout << "x меньше или равно 5" << endl;
    }
    
    // Цикл for
    for (int i = 0; i < 5; ++i) {
        cout << "Итерация: " << i << endl;
    }
    
    // Цикл while
    int count = 0;
    while (count < 3) {
        cout << "Счетчик: " << count << endl;
        ++count;
    }
}
```

## Функции
```cpp
#include <iostream>
using namespace std;

// Функция с параметрами
int add(int a, int b) {
    return a + b;
}

// Функция с несколькими параметрами
void printInfo(string name, int age) {
    cout << "Имя: " << name << endl;
    cout << "Возраст: " << age << endl;
}

int main() {
    int result = add(5, 3);
    cout << "Сумма: " << result << endl;
    
    printInfo("Иван", 25);
}
```

## Указатели и динамическая память
```cpp
#include <iostream>
using namespace std;

int main() {
    // Создание указателя
    int* ptr = new int(42);
    cout << "Значение: " << *ptr << endl;
    
    // Освобождение памяти
    delete ptr;
    
    // Динамический массив
    int size = 5;
    int* arr = new int[size];
    
    for (int i = 0; i < size; ++i) {
        arr[i] = i * 2;
    }
    
    delete[] arr;
}
```
'''
                            },
                            {
                                'name': 'Классы и объектно-ориентированное программирование',
                                'content': '''
# Объектно-ориентированное программирование в C++

## Основные концепции ООП
1. Классы и объекты
2. Инкапсуляция
3. Наследование
4. Полиморфизм

## Определение класса
```cpp
#include <iostream>
#include <string>
using namespace std;

// Класс "Студент"
class Student {
private:
    string name;
    int age;
    double gpa;

public:
    // Конструктор
    Student(string n, int a, double g) : 
        name(n), age(a), gpa(g) {}
    
    // Методы доступа (геттеры)
    string getName() { return name; }
    int getAge() { return age; }
    double getGPA() { return gpa; }
    
    // Метод класса
    void introduce() {
        cout << "Меня зовут " << name 
             << ", мне " << age 
             << " лет, GPA: " << gpa << endl;
    }
};

// Наследование
class GraduateStudent : public Student {
private:
    string research_topic;

public:
    GraduateStudent(string n, int a, double g, string topic) :
        Student(n, a, g), research_topic(topic) {}
    
    void presentResearch() {
        cout << "Тема исследования: " << research_topic << endl;
    }
};
```

## Полиморфизм
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Абстрактный базовый класс
class Shape {
public:
    virtual double area() = 0;  // Чисто виртуальный метод
    virtual void print() = 0;
};

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() override {
        return width * height;
    }
    
    void print() override {
        cout << "Прямоугольник: " 
             << width << " x " << height << endl;
    }
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}
    
    double area() override {
        return 3.14 * radius * radius;
    }
    
    void print() override {
        cout << "Круг: радиус " << radius << endl;
    }
};
```

## Шаблоны (Generics)
```cpp
#include <iostream>
using namespace std;

// Шаблонная функция
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Шаблонный класс
template <typename T>
class Stack {
private:
    T* elements;
    int top;
    int capacity;

public:
    Stack(int size = 10) {
        elements = new T[size];
        capacity = size;
        top = -1;
    }
    
    void push(T value) {
        if (top < capacity - 1) {
            elements[++top] = value;
        }
    }
    
    T pop() {
        if (top >= 0) {
            return elements[top--];
        }
        throw runtime_error("Стек пуст");
    }
};
```
'''
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'Java': {
        'manuals': [
            {
                'name': 'Основы Java',
                'topics': [
                    {
                        'name': 'Введение в Java',
                        'tutorials': [
                            {
                                'name': 'Первое приложение',
                                'content': 'Создаем первую программу на Java'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'Kotlin': {
        'manuals': [
            {
                'name': 'Основы Kotlin',
                'topics': [
                    {
                        'name': 'Введение в Kotlin',
                        'tutorials': [
                            {
                                'name': 'Первая программа',
                                'content': 'Знакомство с синтаксисом Kotlin'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'Ruby': {
        'manuals': [
            {
                'name': 'Основы Ruby',
                'topics': [
                    {
                        'name': 'Введение в Ruby',
                        'tutorials': [
                            {
                                'name': 'Первая программа',
                                'content': 'Начинаем программировать на Ruby'
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

    # Заполнение базы данных
    for lang_name, lang_content in language_contents.items():
        try:
            language = Language.objects.get(name=lang_name)
            
            for manual_data in lang_content['manuals']:
                manual = Manual.objects.create(
                    name=manual_data['name'],
                    language=language,
                    publication_date=date.today()
                )
                
                for topic_data in manual_data['topics']:
                    topic = Topic.objects.create(
                        name=topic_data['name'],
                        manual=manual
                    )
                    
                    for tutorial_data in topic_data['tutorials']:
                        Tutorial.objects.create(
                            name=tutorial_data['name'],
                            content=tutorial_data['content'],
                            topic=topic,
                            publication_date=date.today()
                        )
                
                print(f"Создан учебный материал для {lang_name}")
        
        except Language.DoesNotExist:
            print(f"Язык {lang_name} не найден")

def main():
    create_educational_content()
    print("Учебные материалы успешно добавлены!")

if __name__ == '__main__':
    main()