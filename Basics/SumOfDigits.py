n=int(input("Enter a number to find sum of digits: "))

def sum(n):
    if n==0:
        return 0
    else:
        return n%10 + sum(n//10)

result=sum(n)
print("Sum of Digits: ",result)