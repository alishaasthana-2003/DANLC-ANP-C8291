#Wap to print first 10 prime numbers
import math

def is_prime(number):
    if number<=1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i==0:
            return False
    return True

primeNumbers = []
number=2

while len(primeNumbers) < 20:
    if is_prime(number):
        primeNumbers.append(number)
    number+=1

print("The Fiest 10 prime numbers are:")
print(primeNumbers)