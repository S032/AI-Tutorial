## Туториал по односвязным спискам в Python

Односвязный список — это структура данных, представляющая собой последовательность узлов, где каждый узел хранит данные и ссылку на следующий узел в списке. Последний узел указывает на `None`, обозначая конец списка.

**Преимущества односвязных списков:**

* **Динамический размер:**  В отличие от массивов, списки могут расти или уменьшаться по мере необходимости, что эффективно использует память.
* **Эффективная вставка и удаление:** Вставка и удаление элементов в начале или середине списка происходит быстро, без необходимости сдвига других элементов.

**Недостатки односвязных списков:**

* **Доступ по индексу:** Доступ к элементу по индексу требует прохода по списку с начала, что занимает O(n) времени.
* **Дополнительная память:**  Каждый узел хранит ссылку на следующий элемент, что требует дополнительной памяти по сравнению с массивом.


**Реализация односвязного списка в Python:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None


    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

```

**Пример использования:**

```python
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("C")
llist.append("D")
llist.print_list() # Output: C -> A -> B -> D -> None

llist.delete_node("B")
llist.print_list() # Output: C -> A -> D -> None

llist.delete_node("C")
llist.print_list() # Output: A -> D -> None
```

**Объяснение кода:**

* **Класс `Node`:** Представляет отдельный узел списка, содержащий данные (`data`) и ссылку на следующий узел (`next`).
* **Класс `LinkedList`:**  Реализует сам односвязный список.
    * `__init__`:  Инициализирует пустой список, устанавливая `head` в `None`.
    * `append`: Добавляет новый узел в конец списка.
    * `prepend`: Добавляет новый узел в начало списка.
    * `delete_node`: Удаляет узел с заданным значением.
    * `print_list`:  Выводит содержимое списка на экран.


**Дополнительные задачи для практики:**

* Реализовать метод `insert_after_node`, который вставляет новый узел после заданного узла.
* Реализовать метод `get_length`, который возвращает длину списка.
* Реализовать метод `reverse`, который переворачивает список.


Этот туториал предоставляет базовые знания об односвязных списках в Python.  Понимание этой структуры данных важно для решения многих задач в программировании.
