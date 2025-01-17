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