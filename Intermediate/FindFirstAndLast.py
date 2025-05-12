n=int(input("Enter a number to find the first and last digit: "))
def first_and_last(n):
    last = n%10
    while n>0:
        first = n%10
        n//=10
    return f"The first digit is: {first} and the last digit is: {last}"
result = first_and_last(n)
print(result)