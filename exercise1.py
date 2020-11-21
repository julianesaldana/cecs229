#Julian Saldana 018462169


#Code:
import math

A = 18462169
birthMonth = 7
B = A % birthMonth
primeNumbers = []
extraCreditPrimeNumbers = []


#odd only
if A % 2 != 0:
    print("A is odd\n")
    print("Cos of", A, "is", math.cos(A))
    print("Tan of", A, "is", math.tan(A))
    print("Log base 10 of", A, "is", math.log10(A))
    print("Log base 8 of", A, "is", math.log(A, 8))
    print(B, "to the power of 8 is", B**8)
    print("Absolute value of (-1)^", B, "*", B, "is", -1**B * B)
    print(A, "/", birthMonth, "rounded up is", math.ceil(A/birthMonth))
    print(A, "/", birthMonth, "rounded down is", math.floor(A/birthMonth))
    print("largest amount between A, B, and birthmonth is", max(A, B, birthMonth))
    print("Smallest amount between A, B, and birthmonth is", min(A, B, birthMonth))
    print("4th root of A is", A**(1 / 4))


#even only
else:
    print("A is even\n")
    print("Sin of", A, "is", math.sin(A))
    print("Cot of", A, "is", (1 / math.tan(A)))
    print("Log base 10 of", A, "is", math.log10(A))
    print("Log base 7 of", A, "is", math.log(A, 7))
    print(B, "to the power of -7 is", B**-7)
    print("Absolute value of (-1)^", B, "*", B, "is", -1**B * B)
    print(A, "/", birthMonth, "rounded up is", math.ceil(A/birthMonth))
    print(A, "/", birthMonth, "rounded down is", math.floor(A / birthMonth))
    print("largest amount between A, B, and birthmonth is", max(A, B, birthMonth))
    print("Smallest amount between A, B, and birthmonth is", min(A, B, birthMonth))
    print("5th root of A is", A ** (1 / 5))


#applies to both
print("The quotient of A/B is", A/B)

for num in range(0, 5 * B):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            primeNumbers.append(num)  
print("Finding prime numbers from 0 to 5*B:", primeNumbers)

if -1**B == -1:
    result = True
else:
    result = False
print("Finding if (-1)^B == -1:", result)

name = input("Enter your name: ")
print(name, A)

#extra credit
print("\nExtra credit")
for num in range(B, 5 * B):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            extraCreditPrimeNumbers.append(num) 
print("Prime numbers from B to 5*B:", extraCreditPrimeNumbers)


'''Results:
A is odd

Cos of 18462169 is -0.9629617136610379
Tan of 18462169 is -0.28000922307003295
Log base 10 of 18462169 is 7.266282722117588
Log base 8 of 18462169 is 8.04602290666568
5 to the power of 8 is 390625
Absolute value of (-1)^ 5 * 5 is -5
18462169 / 7 rounded up is 2637453
18462169 / 7 rounded down is 2637452
largest amount between A, B, and birthmonth is 18462169
Smallest amount between A, B, and birthmonth is 5
4th root of A is 65.54969579281337
The quotient of A/B is 3692433.8
Finding prime numbers from 0 to 5*B: [2, 3, 5, 7, 11, 13, 17, 19, 23]
Finding if (-1)^B == -1: True

Enter your name: Julian
Julian 18462169

Extra credit
Prime numbers from B to 5*B: [5, 7, 11, 13, 17, 19, 23]
'''