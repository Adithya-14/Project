n=int(input("Enter a number to find the largest number: "))
def largest(n):
    largest = 0
    while n>0:
        digit = n%10
        n//=10
        if digit>largest:
            largest=digit
    return f"The largest digit in the number is: {largest}"
result = largest(n)
print(result)