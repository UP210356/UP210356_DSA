class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data


# FIFO = PEPS
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if not self.head else False
    
    def enqueue(self, data):
        newNode = Node(data)
        self.size += 1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def dequeue(self):
        l = self.getSize()
        Data = self.tail.data
        self.tail = self.head
        for i in range(l):
            self.head.next = self.tail
        self.size -= 1 
        return Data
    
    def show(self):
        D2 = self.head.data
        l = self.size
        for i in range(l-1):
            self.head = self.head.next
            D1 = self.head.data
            D2 = D2 + "  " + D1
        return D2
    
    def exist(self, data):
        a = self.head.data
        l = self.size
        for i in range(l-1):
            self.head = self.head.next
            if a == data:
                return True
            else:
                continue
        return False
    

q = Queue()
q.enqueue("Jose")
q.enqueue("Maria")
q.enqueue("Jesus")
print(q.exist("Maria"))
