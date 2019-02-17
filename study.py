class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def GetData(self):
        return self.data
    def SetData(self,data):
        self.data = data
    def GetNext(self):
        return self.next
    def SetNext(self,next):
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
    def Push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            current = self.top
            while current.GetNext() != None:
                current = current.GetNext()
            current.SetNext(new_node)
    def Pop(self):
        current = self.top
        if current.GetNext() == None:
            self.__init__()
            return current.GetData()
        while current.GetNext() != None:
            previous = current
            current = current.GetNext()
        previous.SetNext(None)
        return current.GetData()
    def Peek(self):
        current = self.top
        while current.GetNext() != None:
            current = current.GetNext()
        return current.GetData()