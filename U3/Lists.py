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

    def delData(self, item):
        si = self.search(item)
        if si != None:
            actual = self.cabeza
            pos=0
            previo = None
            encontrado = False
            while not encontrado:
                if actual.obtenerDato() == item:
                    encontrado = True
                else:
                    previo = actual
                    actual = actual.obtenerSiguiente()
                pos+=1
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
            self.size-=1
            return pos
        else: return None

    def delPos(self, pos):
        dato = self.seek(pos)
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == dato:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
        self.size-=1
        return dato

    def printIzq(self):
        current = self.cabeza
        while current is not None:
            print(current.dato)
            current = current.siguiente

    def printDer(self):
        stack = []
        current = self.cabeza
        while current is not None:
            stack.append(current.dato)
            current = current.siguiente
        while stack:
            print(stack.pop())
    

L = List()
L.insert(56)
L.insert(2)
L.insert(34)
L.insert(100)
L.insert(200)
#2,34,56,100,200
'''
print(L.delPos(2))
print('---')
L.printIzq()
'''
'''
print(L.delData(34))
print('---')
L.printIzq()
'''
'''
print(L.seek(3))
print(L.search(200))
'''
'''
L.printDer()
'''

#insert
#delPos
#delData
#search(dato)
#seek(pos)
#printIzq
#printder