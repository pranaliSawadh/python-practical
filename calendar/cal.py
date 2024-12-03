def calendar():
    cal_grid = initialize()
    user_interface(cal_grid)

def initialize():
    cal_grid = [[" " for _ in range(7)] for _ in range(7)]
    return cal_grid

def user_interface(cal_grid):
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    display_month(year, month)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def get_first_day_of_year(day_of_month, month, year):
    if month == 1 or month == 2:  # January and February as months 13 and 14
        month += 12
        year -= 1
    k = day_of_month
    m = month
    D = year % 100
    C = year // 100
    f = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - (2 * C)
    fmod7 = f % 7
    fmod7_day = {0: "Sat", 1: "Sun", 2: "Mon", 3: "Tue", 4: "Wed", 5: "Thu", 6: "Fri"}
    return fmod7_day[fmod7]
    
    
def display_month(year, month):
    calendar_months = ["January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"]
    day_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Now using the correct calendar_months list to print month name
    print(f"{calendar_months[month - 1]} {year}".center(35, "*"))
    print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun")

    day = get_first_day_of_year(1, month, year)
    start_day_index = list(days).index(day)

    # Print leading spaces for the first day
    print("     " * start_day_index, end="")

    date = 1
    for _ in range(start_day_index, 7):
        if date <= day_in_month[month - 1]:
            print(f"  {date:02} ", end="|")
            date += 1
        else:
            break
    print("\n" + "-----" * 7)

    # Fill remaining dates in the month
    while date <= day_in_month[month - 1]:
        for _ in range(7):
            if date <= day_in_month[month - 1]:
                print(f"  {date:02} ", end="|")
                date += 1
            else:
                break
        print("\n" + "-----" * 7)


def display_year_calendar(year):
    for month in range(1, 13):
        display_month(year, month)

calendar()

