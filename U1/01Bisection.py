print('The secret number is between 1-1000\n')
secret= 1000
n = int(input('Guess the secret number: '))
i=1
while n != secret:
    i+=1
    if n < secret: 
        n = (int(input('Enter a higher number: ')))
    elif n > secret:
        n = (int(input('Enter a lower number: ')))
print('Secret number: ', n)
print('Number of attempts: ', i)