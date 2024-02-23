# String Palindrome

'''
def palindrome(name):
    if name == name[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
'''


def palindrome(name):
    for i in range(0, int(len(name)/2)):
        if name[i] != name[len(name) - i - 1]:
            return False

    return True


is_palindrome = palindrome(input("Enter a string to verify if it is a Palindrome:"))

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


# Number Palindrome

num = int(input("Enter a number to verify if it is a Palindrome: "))
temp = num
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if temp == rev:
    print("Yes")
else:
    print("No")