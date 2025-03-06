import math

num = input("Enter Number: ")
num1 = int(num)

if num1 < 2:
    print("Not a prime number")  
else:
    for n in range(2, int(math.sqrt(num1)) + 1):
        if num1 % n == 0:
            print("Not a prime number")
            break
    else:  
        print("Prime number")

