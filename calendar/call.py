import calendar

def display_year_calendar(year, rows, cols, separator):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Prepare a list to hold the month strings
    month_strings = []

    # Generate month strings for each month in the year
    for month in range(1, 13):
        month_str = cal.formatmonth(year, month)
        month_strings.append(month_str)

    # Calculate the maximum number of lines in each month
    max_lines = max(len(month.splitlines()) for month in month_strings)

    # Print the calendar with separators
    for row in range(rows):
        for line in range(max_lines):
            for col in range(cols):
                month_index = row * cols + col
                if month_index < 12:
                    # Get the current month's string and split it into lines
                    month_lines = month_strings[month_index].splitlines()
                    # Print the corresponding line or empty space if it doesn't exist
                    if line < len(month_lines):
                        print(month_lines[line].ljust(20), end=' ')
                    else:
                        print(' ' * 20, end=' ')
                # Print vertical separator
                if col < cols - 1 and month_index < 12:
                    print(separator.ljust(5), end=' ')
            print()  # New line after each row of months

        # Print horizontal separator after each row of months except the last row
        if row < rows - 1:
            print(separator * (20 * cols + 5 * (cols - 1)))

# User input for year, rows, columns, and separator
year = int(input("Enter the year: "))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
separator = input("Enter a separator (e.g., *, |, #, !, ^): ")

# Display the calendar
display_year_calendar(year, rows, cols, separator)
