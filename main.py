num = int(input("Enter number for calculate the sum"))
sum: int = 0
while num > 0:
    sum = sum + num
    num = num - 1
print("here is the sum", sum)

year = int(input("Enter the year: "))
while year != 0:
    if (year % 4) == 0 and (year % 100) != 0:
        print(year, "is a leap year")
    else:
        if ((year % 100) == 0) and ((year % 400) == 0):
            print("the year is leap year")
        else:
            print("the year is not leap")
    year= int(input("Enter the year"))
