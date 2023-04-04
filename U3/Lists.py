class Node:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class List:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size=0

    def estaVacia(self):
        return self.cabeza == None
    
    def search(self,item):
        actual = self.cabeza
        pos = 0
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()
            pos+=1
        if encontrado == True:
            return pos
        else:
            return encontrado
    
    def seek(self, pos):
        actual = self.cabeza
        if pos < self.size:
            for i in range(pos):
                actual = actual.siguiente
            return actual.dato
        else:
            return None
    
    def insert(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        temp = Node(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)
        self.size+=1

    def delData(self, data):
        pass

    def delpos(self, pos):
        pass

    def printIzq(self):
        nodo = self.cabeza
        while nodo is not None:
            print(nodo.dato, end= ' ')
            nodo = nodo.siguiente
        print()

    def printDer(self):
        nodo = self.cabeza
        while nodo is not None:
            print(nodo.dato, end= ' ')
            nodo = nodo.siguiente
        print()

L = List()
L.insert(56)
L.insert(2)
L.insert(34)
L.insert(100)
print(L.size)
print(L.seek(4))