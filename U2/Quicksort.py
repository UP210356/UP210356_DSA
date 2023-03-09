import random
def quicksort (a, p, u):
    c = (p + u)//2
    i = p
    j = u
    pivote = a[c]
    while i <= j:
        while a[i] < pivote:
            i+=1
        while a[j] > pivote:
            j-=1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1
    if p < j:
        quicksort(a, p, j)
    if i < u:
        quicksort(a, i, u)
    return a

def BinarySearch(datos,elemento):
    li = 0
    ls = len(a)-1
    prin = li
    final = ls
    mit = int((prin + final)//2)
    con = 0

    while prin <= final and datos[mit != elemento]:
        if elemento < datos[mit]:
            final = mit -1
        else:
            prin = mit + 1
        mit = int((prin + final)//2)
        con += 1
    if datos[mit] == elemento:
        pos = mit
    else:
        pos = False
    
    return pos, con

a = []
def unico(x,a):
  esUnico=True
  for i in range(len(a)):
    if x==a[i]:
      esUnico=False
      break
  return esUnico

def fillArray(n):
    for f in range(n):
        x = random.randint(101,500)
        if unico(x,a):
            a.append(x)
    return a

print(quicksort(fillArray(100), 0, len(a)-1))
print(BinarySearch(quicksort(fillArray(100), 0, len(a)-1), 108))