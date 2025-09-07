# Taking input from the user
year = int(input("Enter a year: "))

# Condition to check leap year
if (year % 400 == 0):
    print(year, "is a Leap Year")
elif (year % 100 == 0):
    print(year, "is NOT a Leap Year")
elif (year % 4 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
