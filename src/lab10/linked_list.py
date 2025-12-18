

class Node:
    def __init__(self,value: any,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return self.value



class SinglyLinkedList:
    def __init__(self):
        self.head = None # первый элемент списка (голова)
        self.tail = None # Последний элемент списка (хвост)
        self._size = 0 # кол-во элементов в списке

    def append(self,value) -> None:
        new=Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self._size += 1

    def prepend(self,value) -> None:
        new = Node(value,next=self.head)
        self.head=new
        self._size += 1
        if self.tail is None: self.tail = new
    
    def insert(self,idx: int, value) -> None:
        if idx<0 or idx>self._size:
            raise IndexError("Неверно указан индекс")
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for i in range(idx-1):
                current = current.next
            new = Node(value,next=current.next)
            current.next=new
            self._size += 1
    
    def remove_at(self,idx: int) -> None:
        if idx<0 or idx>=self._size:
            raise IndexError("Неверно указан индекс")
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
    
    def b_out(self):
        string=""
        current = self.head
        for x in range(self._size,0,-1):
            string+=" >- "+str(current)
            current = current.next
        string="enoN"+string
        return string[::-1]
