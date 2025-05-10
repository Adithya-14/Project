n=int(input("Enter a number to count: "))
def ocunt(n):
    count=0
    if n==0:
        return 0
    else:
        count+=1
        return count + ocunt(n//10)
result=ocunt(n)
print("No of Digits: ",result)

# The code is a simple recursive function to count the number of digits in a given integer.

def countr(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
result = countr(n)
print("Count of Digits: ", result)