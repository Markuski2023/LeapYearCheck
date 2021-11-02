
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        print("Its a leap year")
        return True
    elif year % 400 == 0:
        print("Its a leap year")
        return True
    elif year % 4 != 0:
        print("Its NOT a leap year")
        return False
    elif year % 100 == 0 and year % 400 != 0:
        print("Its NOT a leap year")
        return False