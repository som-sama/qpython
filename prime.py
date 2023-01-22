import math
i = 0
temp = 0
n = int(input("Enter the number: "))
if n == 0 or  n == 1:
    print("Its neither prime nor composite")
else:
    temp = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp = 1
            break
    if temp == 1:
        print("Its not a prime number")
    else:
        print("Its a prime number ")