def calendar():
    year = int(input("Enter the year: "))
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    separator = input("Enter a separator (*, |, #, !, ^): ")
    display_year_calendar(year, rows, cols, separator)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_first_day_of_month(month, year):
    if month < 3:
        month += 12
        year -= 1
    k = 1  # Day of the month
    D = year % 100
    C = year // 100
    f = k + (13 * (month + 1)) // 5 + D + (D // 4) + (C // 4) - (2 * C)
    fmod7 = f % 7
    fmod7_day = {0: "Sat", 1: "Sun", 2: "Mon", 3: "Tue", 4: "Wed", 5: "Thu", 6: "Fri"}
    return fmod7_day[fmod7]

def display_month(year, month):
    if is_leap_year(year):
        day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]

    start_day = get_first_day_of_month(month, year)
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    start_day_index = days_of_week.index(start_day)

    # Prepare month header and weekdays
    header = f"{month_names[month - 1]} {year}".center(20)
    weekdays = " Mon  Tue  Wed  Thu  Fri  Sat  Sun "
    
    # Generate month layout
    calendar_lines = [header, weekdays]
    line = "     " * start_day_index
    date = 1

    # Fill days of the month
    for _ in range(start_day_index, 7):
        if date <= day_in_month[month - 1]:
            line += f"{date:3}  "
            date += 1
        else:
            line += "     "  # Empty space for unused dates
    calendar_lines.append(line)

    while date <= day_in_month[month - 1]:
        line = ""
        for _ in range(7):
            if date <= day_in_month[month - 1]:
                line += f"{date:3}  "
                date += 1
            else:
                line += "     "  # Empty space for unused dates
        calendar_lines.append(line)

    return calendar_lines

def display_year_calendar(year, rows, cols, separator):
    if rows * cols < 12:
        print("Insufficient cells to display all months. Please increase rows or columns.")
        return

    all_months = [display_month(year, month) for month in range(1, 13)]
    current_month = 0

    for row in range(rows):
        if current_month >= 12:
            break
        max_lines = max(len(all_months[m]) for m in range(current_month, min(current_month + cols, 12)))
        
        # Print lines row-wise
        for line_index in range(max_lines):
            for col in range(cols):
                if current_month + col < 12:
                    month_lines = all_months[current_month + col]
                    if line_index < len(month_lines):
                        print(month_lines[line_index].ljust(25), end="")
                    else:
                        print(" " * 25, end="")
                # Print vertical separator after each month except the last one in the row
                if col < cols - 1 and current_month + col < 12:
                    print(separator.ljust(5), end="")
            print()
        
        # Print horizontal separator after each row of months except the last row
        if current_month + cols < 12:
            print(separator * ( 25 * cols + 5 * (cols - 1)) )

        current_month += cols

calendar()
