n=int(input("Enetr a number to find the increasing order: "))
def increasing_order(n):
    digits = []
    while n>0:
        digit = n%10
        digits.append(digit)
        n//=10
    digits.sort()
    dig=''.join(map(str, digits))
    if dig==n:
        return f"The digits are already in increasing order.{n}"
    else:
        return f"The increasing order of the digits is: {dig}"

result = increasing_order(n)
print(result)