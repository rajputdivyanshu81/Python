def factorial(n):
    if(n==1 or n==0):
     return 1
    return n * factorial(n-1)

n = int(input("enter the number :"))
print(f"the factorial of this number is: {factorial(n)} ")

# basically recursion means to say that calling the prevuious again and again