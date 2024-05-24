# To find if a number is prime
import math


def prime(n):
    # Find the square root of the number and see if divisible up to that number
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Please provide a number: "))

result = prime(num)

if result:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")