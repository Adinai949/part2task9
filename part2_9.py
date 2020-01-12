
n = int(input('Введите число: '))
factorial = 1 
if n < 0:
    n = n* -1
    for number in range(1, n+1):
        factorial= factorial*number
        print(factorial)
elif n == 0:
    print('0')
else:
    for number in range(1, n+1):
        factorial= factorial*number
        print(factorial)
        
