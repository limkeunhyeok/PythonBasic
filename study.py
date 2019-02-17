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

class LinkedList:
    def __init__(self):
        self.top = None
    def Add(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            current = self.top
            while current.GetNext() != None:
                current = current.GetNext()
            current.SetNext(new_node)
    def Remove(self):
        if self.top == None:
            print("empty")
        else:
            current = self.top
            previous = current
            while current.GetNext() != None:
                previous = current
                current = current.GetNext()
            previous.SetNext(None)
            return current.GetData()
    def Count(self):
        count = 1
        current = self.top
        if self.top == None:
            return 0
        while current.GetNext() != None:
            current = current.GetNext()
            count += 1
        return count
    def Clear(self):
        self.__init__()
    def Contains(self,data):
        current = self.top
        count = 0
        for i in range(self.Count()):
            if current.GetData() == data:
                print('%d는 %d번째에 있습니다.' % (data, count))
            current = current.GetNext()
            count += 1
    def Sort(self):
        current = self.top
        previous = current
        for i in range(self.Count() - 1):
            for j in range(self.Count() - 1):
                previous = current
                current = current.GetNext()
                if current.GetData() < previous.GetData():
                    value1 = current.GetData()
                    value2 = previous.GetData()
                    current.SetData(value2)
                    previous.SetData(value1)
            current = self.top
    def PrintList(self):
        if self.top != None:
            current = self.top
            print(current.GetData(),end = ' ')
            while current.GetNext() != None:
                current = current.GetNext()
                if current.GetNext() == None:
                    print(current.GetData())
                else:
                    print(current.GetData(), end = ' ')


list = LinkedList()
print(list.Count())
list.PrintList()
list.Sort()
list.PrintList()
print(list.Count())