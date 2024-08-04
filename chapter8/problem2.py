'''
sum(n) = 1 + 2 + 3 + 4 + .....n
'''


def sum(n):
    if(n==1):
     return 1
    return n + sum(n-1)

n = int(input("enter the number :"))
print(f"the sum of this number is: {sum(n)} ")

# basically recursion means to say that calling the prevuious again and again
