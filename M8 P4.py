#Greg Brewer
#6/4/23
#Problem Write a function that takes a year as a parameter and returns True if the year is a
#leap year, False if it is otherwise.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage:
year = 2024
result = is_leap_year(year)
print(result)
