#a program to reverse an integer in Python.
def reverse(n):
    rev = 0
    while(n>0):
        rem  = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev


n = int(input("Enter a number "))
print("Number before reverse is", n)
print("The numbere after reverse is", reverse(n))