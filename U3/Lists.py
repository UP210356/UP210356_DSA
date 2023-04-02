class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def asignData(self, next):
        self.data = next

    def asignNext(self, new):
        self.next = new
    
class List:
    def insert(self, data):
        act = self.cabeza
        prev = None
        detenerse = False
        while act != None and not detenerse:
            if act.getData() > data:
                detenerse = True
            else:
                prev = act
                act = act.getNext()

        temp = Node(data)
        if prev == None:
            temp.asignNext(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignNext(act)
            prev.asignNext(temp)
            
    def deldat(self, data):
        pass

    def delpos(self, pos):
        pass

    def getSize(self):
        pass

    def search(self, data):
        actual = self.head
        found = False
        stop = False
        while actual != None and not found and not stop:
            if actual.obtenerDato() == data:
                encontrado = True
            else:
                if actual.obtenerDato() > data:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

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
print(q.show())