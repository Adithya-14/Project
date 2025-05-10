n=int(input("Enter a number to reverse: "))

def reverse(n):
    origin=n
    while n > 0:
        digit = n % 10
        n //= 10
        print(digit, end="")
    print() # Print a newline after reversing the number
result = reverse(n)
print(result)