class Node:
    def __init__(self,value: any,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return self.value
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self._size = 0 

    def append(self,value) -> None:
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self,value) -> None:
        new_node = Node(value,next=self.head)
        self.head=new_node
        self._size += 1
        if self.tail is None: self.tail = new_node
    
    def insert(self,idx: int, value) -> None:
        if idx<0 or idx>self._size:
            raise IndexError("Задайте верный индекс")
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            new_node = Node(value,next=current.next)
            current.next=new_node
            self._size += 1
    
    def remove_at(self,idx: int) -> None:
        if idx<0 or idx>=self._size:
            raise IndexError("Задайте верный индекс")
        if idx == 0:
            self.head=self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None
            return None
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            current.next=current.next.next
            if current.next is None: self.tail = current
            self._size -= 1
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    


if __name__=="__main__":
    print("----------------- Тестирование SinglyLinkedList -----------------")



sll = SinglyLinkedList()

print(f"__len__() --> {len(sll)} (0)")

print(f"list(sll) --> {list(sll)} ([])")



sll.append("A")

print(f"append('A') --> список: {list(sll)} (['A'])")

print(f"__len__() --> {len(sll)} (1)")



sll.append("B")

sll.append("C")

print(f"append('B'), append('C') --> список: {list(sll)} (['A', 'B', 'C'])")

print(f"__len__() --> {len(sll)} (3)")



sll.prepend("начало")

print(f"prepend('начало') --> список: {list(sll)} (['начало', 'A', 'B', 'C'])")

print(f"__len__() --> {len(sll)} (4)")



sll.insert(2, "вставка")

print(f"insert(2, 'вставка') --> список: {list(sll)} (['начало', 'A', 'вставка', 'B', 'C'])")

print(f"__len__() --> {len(sll)} (5)")



sll.remove_at(1)

print(f"remove_at(1) --> список: {list(sll)} (['начало', 'вставка', 'B', 'C'])")

print(f"__len__() --> {len(sll)} (4)")



print(f"__repr__() --> {repr(sll)} (SinglyLinkedList(['начало', 'вставка', 'B', 'C']))")



sll.remove_at(3)

print(f"remove_at(3) --> список: {list(sll)} (['начало', 'вставка', 'B'])")

print(f"__len__() --> {len(sll)} (3)")