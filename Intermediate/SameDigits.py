n=int(input("ENter a number to find the same digits: "))
def same_digits(n):
    l=n%10
    a=True
    while n>0:
        digit=n%10
        if digit!=l:
            a=False
            break
        n//=10
    return a
result = same_digits(n)
if result:
    print(f"The number {n} has same digits.")
else:
    print(f"The number {n} does not have same digits.")