# To print the fibonacci series
# 0 1 1 2 3 5 8 13 21


def fib(num):
    if num < 0:
        print("wrong")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)


n = 7
print(fib(n))