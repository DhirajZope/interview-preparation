class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None

    def iter(self):
        if self.__head is None:
            print("Empty List")
            return -1

        else:
            n = self.__head
            while n is not None:
                print(n.data, end=" ")
                n = n.next


    def add_begin(self, data):
        newNode = Node(data)
        newNode.next = self.__head
        self.__head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            n = self.__head
            while n.next is not None:
                n = n.next
            n.next = newNode

    def insert(self, data, value):
        n = self.__head
        while n is not None:
            if n.data == value:
                break
            n = n.next

        if n is None:
            print("Value Not found")
            return -1
        else:
            newNode = Node(data)
            newNode.next = n.next
            n.next = newNode
    
    def insertAt(self, data, index):
        currentIndex = 0
        n = self.__head
        while currentIndex+1 != index and n is not None:
            n = n.next
            currentIndex += 1
        if n is None:
            print("List index out of range")
            return -1
        else:
            newNode = Node(data)
            newNode.next = n.next
            n.next = newNode

    def len(self):
        counter = 0
        n = self.__head
        while n is not None:
            counter += 1
            n = n.next
        return counter

    def delete_begin(self):
        if self.__head is None:
            print("Empty Linked List")
            return
        temp = self.__head
        self.__head = self.__head.next
        del temp

    def pop(self):
        if self.__head is None:
            print("Empty Linked List")
            return
        n = self.__head
        while n.next is not None:
            prev = n
            n = n.next
        prev.next = None
        return n.data

    def deleteAt(self, index):
        if self.__head is None:
            print("Empty List")
            return
        currentIndex = 0
        n = self.__head
        while currentIndex != index and n is not None:
            currentIndex += 1
            prev = n
            n = n.next
        if n is None:
            print("List Index out of bounds")
            return
        prev.next = n.next
        del n

    def pop2(self):
        if self.__head is None:
            print("Empty Linked List")
            return
        n = self.__head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def update(self, index, data):
        if self.__head is None:
            print("List is empty")
            return
        n = self.__head
        currentIndex = 0
        while currentIndex != index and n is not None:
            n = n.next
            currentIndex += 1
        n.data = data


List = LinkedList()
List.add_begin(10)
List.add_begin(20)

List.append(30)
List.append(40)

List.insert(50, 10)

List.insertAt(5, 2)

# List.delete_begin()

# print(List.len())
# print(List.pop())
List.iter()
# List.deleteAt(2)
# List.pop2()
print()
List.update(2, 60)
List.iter()