from random import randint

def fillArray(n):
    array = []
    for f in range(n):
        row2 = []
        for c in range(n):
            row2.append(randint(1,100))
        array.append(row2)
    return array

print(fillArray(4))