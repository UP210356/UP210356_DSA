import random
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
 
print(fillArray(100))