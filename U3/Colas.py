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
        