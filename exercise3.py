# Julian Saldana 018462169

ID = 18462169

# question 1
grade = 60 + (ID % 33)

if 60 <= grade <= 70:
    grade = 1.25 * grade
elif 70 <= grade <= 80:
    grade = 1.2 * grade
elif 80 <= grade <= 90:
    grade = 1.15 * grade
elif 90 <= grade <= 100:
    grade = 1.1 * grade
print("1) Final grade is", grade, "\n")

# question 2
userInput = int(input("2) Enter a number: "))
totalSum = 0
for i in range(1, userInput + 1, 1):
    totalSum += i
avg = totalSum / userInput
print("Sum from 1 to %d is %d and average is %.2f\n" % (userInput, totalSum, avg))

# question 3
birthMonth = 7
for i in range(12):
    if i > 8:
        print("%d) Birth month + 6 : %s" % ((i + 1), (str(birthMonth + 6) * (i + 1))))
    else:
        print("%d) %s" % ((i + 1), (str(i + 1) * (i + 1))))
print()

# question 4
