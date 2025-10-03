# (11) A magic date is a date where the date multiplied by the month is equal to the two-digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60 which is the two-digit year. Write a function that determines whether
# or not a date is a magic date. Use your function to create a main program that finds
# and displays all of the magic dates in the 20th century.

#function checking if a date given by user is a magic date or not
def magic_date():
    D=int(input("Enter the date:"))
    M=int(input("Enter the month:"))
    Y=int(input("Enter the year:"))
    if (D * M) == (Y % 100):
        print("It is a magical date.")
    else:
        print("It is not a magic date.")
magic_date()


#function without the user input
def magic_date(D,M,Y):
    if (D * M) == (Y % 100):
        return True
    else:
        return False

#main program
for Y in range(1900,2000):
    for M in range(1,13):
        for D in range(1,32):
            if magic_date(D,M,Y)==True:
                print(f'{D}/{M}/{Y}')