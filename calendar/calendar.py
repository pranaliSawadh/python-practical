def calendar():
	cal_grid = initialize()
	year = int(input("Enter the year : "))
	display_year_calendar(year)
	#user_interface(cal_grid)
	
def initialize():
	cal_grid = [[" " for _ in range(7)] for _ in range(7)]
	return cal_grid
	
def is_leap_year(year):
	if (year%4==0 and year%100!=0)or(year % 400 == 0):
		return True
	else:
		return False

def get_first_day_of_year(month,year):
	k = 1
	m = month
	if month ==1 or month == 2:
		year-=1
	if month ==1 :
		m=13
	if month==2:
		m = 14
	D = year%100
	C = year//100
	f = k + ((13*(m+1))//5)+D+(D//4)+(C//4)-(2*C)	#Zellars Formula
	fmod7 = f%7
	fmod7_day = {0:"Sat",1:"Sun",2:"Mon",3:"Tue",4:"Wed",5:"Thu",6:"Fri"}
	return fmod7_day[fmod7]
		
def display_month(year, month):
    # Determine days in each month
    if is_leap_year(year):
        day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_names = ["January", "February", "March", "April", "May", "June", "July", 
                   "August", "September", "October", "November", "December"]
    
    start_day = get_first_day_of_year(month, year)
    
    print(f"{month_names[month - 1]} {year}".center(28, " "))
    print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun")

    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    start_day_index = days_of_week.index(start_day)
    
    print("     " * start_day_index, end="")

    
# Fill the first week
    date = 1
    for row in range(start_day_index, 7):  
        if date <= day_in_month[month - 1]:
            print(f"{date:3} ", end="|")
            date += 1
        else:
            break
    print("\n" + "-----" * 7)

    # Fill remaining weeks
    while date <= day_in_month[month - 1]:
        for i in range(7):
            if date <= day_in_month[month - 1]:
                print(f"{date:3} ", end="|")
                date += 1
            else:
                break
        print("\n" + "-----" * 7)


def display_year_calendar(year):
	for month in range(1,13):
		display_month(year,month)

calendar()
