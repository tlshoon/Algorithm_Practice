class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = None


class LinkedList(object) :
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)


