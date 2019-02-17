class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if self.is_empty():
            return False
        value = self.head.data
        self.head = self.head.next
        return value
    def peek(self):
        if self.is_empty():
            return False
        return self.head.data