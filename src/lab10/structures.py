from collections import deque
from dataclasses import dataclass
from typing import Any


class Stack:
    def __init__(self):
        self._data: list[Any] = []
    
    def push(self,item) -> None: #Добавить элемент на вершину стека.
        self._data.append(item)

    def pop(self) -> Any: #Снять верхний элемент стека и вернуть его.
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data.pop() # pop - встроенная функция. 

    def peek(self) -> Any | None: #Вернуть верхний элемент без удаления
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool: #Вернуть True, если стек пуст, иначе False.
        return not self._data
    
    def __len__(self) ->  int: #количество элементов в стеке.
        return len(self._data)

class Queue:
    def __init__(self, max_size: int|None = None):
        self._data=deque(maxlen=max_size) #maxlen=max_size - создает очередь с fix size
    
    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

if __name__ == "__main__":
    stack = Stack()
    print(f"Создан стек: {stack._data}")
    

    print(f"   is_empty(): {stack.is_empty()} (ожидается True)")
    print(f"   __len__(): {len(stack)} (ожидается 0)")
    print(f"   peek(): {stack.peek()} (ожидается None)")
    

    stack.push("Первый")
    stack.push("Второй")
    stack.push("Третий")
    print(f"   После push('Первый'), push('Второй'), push('Третий'):")
    print(f"   Стек: {stack._data}")
    print(f"   is_empty(): {stack.is_empty()} (ожидается False)")
    print(f"   __len__(): {len(stack)} (ожидается 3)")
    print(f"   peek(): {stack.peek()} (ожидается 'Третий')")
    

    print(f"   pop(): {stack.pop()} (ожидается 'Третий')")
    print(f"   Остался стек: {stack._data}")
    print(f"   pop(): {stack.pop()} (ожидается 'Второй')")
    print(f"   pop(): {stack.pop()} (ожидается 'Первый')")
    print(f"   После всех pop: {stack._data}")
    print(f"   is_empty(): {stack.is_empty()} (ожидается True)")





    print("================= Тестирование Queue ================")
    

    queue = Queue()
    print(f"Создана очередь: {list(queue._data)}")
    

    print("\n1. Проверка пустой очереди:")
    print(f"   is_empty(): {queue.is_empty()} (ожидается True)")
    print(f"   __len__(): {len(queue)} (ожидается 0)")
    print(f"   peek(): {queue.peek()} (ожидается None)")
    

    queue.enqueue("Клиент A")
    queue.enqueue("Клиент B")
    queue.enqueue("Клиент C")
    print(f"   После enqueue('A'), enqueue('B'), enqueue('C'):")
    print(f"   Очередь: {list(queue._data)}")
    print(f"   is_empty(): {queue.is_empty()} (ожидается False)")
    print(f"   __len__(): {len(queue)} (ожидается 3)")
    print(f"   peek(): {queue.peek()} (ожидается 'Клиент A')")
    

    print(f"   dequeue(): {queue.dequeue()} (ожидается 'Клиент A')")
    print(f"   Осталась очередь: {list(queue._data)}")
    print(f"   dequeue(): {queue.dequeue()} (ожидается 'Клиент B')")
    print(f"   dequeue(): {queue.dequeue()} (ожидается 'Клиент C')")
    print(f"   После всех dequeue: {list(queue._data)}")
    print(f"   is_empty(): {queue.is_empty()} (ожидается True)")
    
    # Тест 4: Ошибка при удалении из пустой очереди
    print("\n4. Попытка удалить из пустой очереди:")
    try:
        queue.dequeue()
        print("ОШИБКА: исключение не вызвано!")
    except IndexError as e:
        print(f"Исключение вызвано: {e}")
    


    limited_queue = Queue(max_size=3)
    limited_queue.enqueue(1)
    limited_queue.enqueue(2)
    limited_queue.enqueue(3)
    print(f"   Добавили 1, 2, 3: {list(limited_queue._data)}")
    limited_queue.enqueue(4)
    print(f"   Добавили 4 (должен удалить 1): {list(limited_queue._data)}")
    print(f"   Размер: {len(limited_queue)} (все равно 3)")