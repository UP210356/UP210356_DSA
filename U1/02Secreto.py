s= 1000
n = int(input('Adivina el número: '))
i=1

while n != s:
    if n < s: 
        n = (int(input('Más alto: ')))
    else:
        n = (int(input('Más bajo: ')))
    i+=1
print('Ganaste!')
print('Intentos: ', i)