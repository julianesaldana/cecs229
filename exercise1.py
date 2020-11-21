import math

A = 18462169
birthMonth = 7
B = A % birthMonth
primeNumbers = []
extraCreditPrimeNumbers = []

#odd
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

#even
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

for x in range(5 * B):
    if x % 2 != 0:
        primeNumbers.append(x)
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
for x in range(B, 5*B):
    if x % 2 != 0:
        extraCreditPrimeNumbers.append(x)
print("Prime numbers from B to 5*B:", extraCreditPrimeNumbers)
