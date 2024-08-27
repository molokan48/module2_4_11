limit = int(input('Введите число до которого нужно разделить числа на "простые" и "не очень"))):  '))
numbers = []
for i in range(1,limit):
    numbers.append(i)
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] !=1:
        for j in range( 2 , numbers[i] ):
           if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            break
        else: primes.append(numbers[i])
print('primes' , primes)
print('not_primes' , not_primes)