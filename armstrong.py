n = int(input("Enter a number"))
i = 0
result = 0
number = n
temp = n 

while n!= 0:
    n = n // 10
    i = i + 1


while number != 0:
    n = number % 10
    result = result + pow(n,i)
    number = number // 10

if temp == result:
    print("Number is armstrong")
else:
    print("Number is not armstrong")