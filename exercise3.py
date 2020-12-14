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
print("3)")
birthMonth = 7
for i in range(12):
    if i > 8:
        print("Birth month + 6 : %s" % ((str(birthMonth + 6) * (i + 1))))
    else:
        print("%s" % ((str(i + 1) * (i + 1))))
print()

# question 4
print("4)")
f = open("excel file.csv", "r")
info = f.readlines()  # gathering all numbers from excel sheet, every index is a row
f.close()
print(info)

f = open("excel file.csv", "r")
row = f.readline().rstrip("\n").split(",")  # creating list of numbers to reverse
for i in range(len(row)):
    row[i] = int(row[i])  # turned string into int
f.close()
row.sort()
row.reverse()  # sorted from big to smallest

f = open("columns.csv", "w")
for i in range(len(row)):  # storing in columns if numbers were in a row
    f.write(str(row[i]))
    f.write("," * 50)
    f.write("\n")

f.close()

f = open("columns.csv", "r")
print(f.readlines())  # reading out file, printing result
f.close()

f = open("rows.csv", "w")
for i in range(len(row)):  # storing in a row if numbers were in a column
    f.write(str(row[i]))
    f.write(",")
    if row[i] == row[-1]:
        f.write("\n")
f.close()

f = open("rows.csv", "r")
print(f.readlines())  # reading out file, print result
f.close()
