class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty() == False:
            Data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return Data
        else: 
            return None
        
    def peak(self):
        return self.head.data

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

n1=Stack()
n1.push("Jose")
n1.push("Maria")
n1.push("Jesus")
print(n1.show())