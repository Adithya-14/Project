n=int(input("Enter a number to find sum of digits: "))
count=0
def ocunt(n):
    global count
    if n==0:
        return 0
    else:
        count+=1
        return ocunt(n//10)
result=ocunt(n)
print("No of Digits: ",count)