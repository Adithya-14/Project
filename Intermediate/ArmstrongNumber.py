n=int(input("Enter a number to find the armstrong number: "))
def is_armstrong(n):
    count=0
    n1=n
    n2=n
    sum=0
    while n>0:
        digit=n%10
        n//=10
        count+=1
    while n1>0:
        digit=n1%10
        n1//=10
        sum+=digit**count
    
    if sum==n2:
        return f"{n2} is an Armstrong number: {sum}"
    else:
        return f"{n2} is Not an Armstrong number: {sum}"
result = is_armstrong(n)
print(result)