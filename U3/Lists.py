class Node:
    def __init__(self, dato):
        self.data = dato
        self.next = None
    
    def getData(self):
        return self.data
    
    def nextNode(self):
        return self.next
    
    def asignNext(self, newData):
        self.next = newData

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
            return self.head == None
    
    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        elif self.head.data > data:
            self.head, newNode.next = newNode, self.head
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = newNode
                    break
                elif currentNode.next.data >= data:
                    newNode.nextNode = currentNode.nextNode
                    currentNode.nextNode = newNode
                    break
                currentNode = currentNode.nextNode
        self.size += 1
        return self.head.data
        
            
    def deldat(self, data):
        actual = self.head
        previo = None
        encontrado = False
        while not encontrado:
            if actual.data == data:
                encontrado = True
            else:
                previo = actual
                actual = actual.next
        if previo == None:
            self.cabeza = actual.next
        else:
            previo.asignNext(actual.next)
        self.size-=1
        return data

    def delpos(self, pos):
        pass

    def getSize(self):
        return self.size

    def search(self, data):
        act = self.head
        found = False
        stop = False
        while act != None and not found and not stop:
            if act.getData() == data:
                found = True
            else:
                if act.getData() > data:
                    stop = True
                else:
                    act = act.next
        return found
    
    def seek(self, pos):
        pass

    def printIzq(self):
        pass

    def printDer(self):
        pass


L = List()
L.insert(56)
L.insert(2)
L.insert(34)
L.insert(100)
print(L.getSize())