n=int(input("Enter a number to check palindrome: "))
def palindrome(n):
    rev = 0
    original = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return original == rev
result = palindrome(n)
if result:
    print("Palindrome")
else:
    print("Not Palindrome")
# The code is a simple function to check if a given integer is a palindrome.