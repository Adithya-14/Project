n=int(input("enter a number to find the same digits: "))
def same_digits(n):
    n1=n
    n2=n
    count=0
    while n>0:
        digit=n%10
        n//=10
        count+=1
    while n1>0:
        digit=n1%10
        n1//=10
        if digit==count:
            return f"{n2} does not have {count} same digits"
    return f"{n2} has {count} same digits"
result = same_digits(n)
print(result)