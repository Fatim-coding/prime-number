#take two input from user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print("prime numbers between", lower, "and", upper, "are")
#loiterate loop from lower limit toupper limit
for num in range(lower, upper+1):
    # all prime numbers are greater than i
    if num > 1:
        for i in range (2, num):
           if (num % i) == 0:
              break
        else:
         print(num)