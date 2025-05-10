n=int(input("Enter a number to find the product of its digits: "))
def product_of_digits(n):
    product = 1
    while n>0:
        digit=n%10
        product*=digit
        n//=10
    return product
result = product_of_digits(n)
print("The product of the digits is:", result)