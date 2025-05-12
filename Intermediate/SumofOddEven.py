n=int(input("Enter a number to find sum of odd and even numbers: "))
def sum_of_odd_even(n):
    sum_odd=0
    sum_even=0
    while n>0:
        digit=n%10
        n//=10
        if digit%2==0:
            sum_even+=digit
            print("Even number is: ", digit)
        else:
            sum_odd+=digit
            print("Odd number is: ", digit)
    return f"The sum of odd numbers is: {sum_odd} and the sum of even numbers is: {sum_even}"
result = sum_of_odd_even(n)
print(result)