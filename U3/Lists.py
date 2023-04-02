class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

class List:
    def __init__(self, data):
        self.head = None
        self.size = 0

    def insert(self, data):
        act = self.head
        prev = None
        stop = False
        while act != None and not stop:
            if self.head > data:
                stop = True
            else:
                prev = act
                act = self.head.next()
        temp = Node(data)
        if prev == None:
            temp.asignNext(self.head)
            self.cabeza = temp
        else:
            temp.asignNext(act)
            prev.asignNext(temp)
        self.size += 1

    def isEmpty(self):
        return self.head == None
            
    def deldat(self, data):
        act = self.head
        prev = None
        found = False
        while not found:
            if act.getData() == data:
                found = True
            else:
                prev = act
                act = act.getNext()

        if prev == None:
            self.cabeza = act.getNext()
        else:
            prev.asignNext(act.getNext())

    def delpos(self, pos):
        pass

    def getSize(self):
        return self.size

    def search(self, data):
        act = self.head
        found = False
        stop = False
        while actual != None and not found and not stop:
            if act.getData() == data:
                encontrado = True
            else:
                if act.getData() > data:
                    stop = True
                else:
                    actual = actual.getNext()
        return encontrado
    
    def seek(self, pos):
        pass

    def printIzq(self):
        pass

    def printDer(self):
        pass


q = List()
q.insert(56)
q.insert(2)
q.insert(34)
print(q.getSize())