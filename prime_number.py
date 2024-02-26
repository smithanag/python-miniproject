# To find if a number is prime

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("Please provide a number: "))

result = prime(num)

if result:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")