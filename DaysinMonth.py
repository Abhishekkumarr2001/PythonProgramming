def leap_year(year):
    leapyear=False
    if year%4==0:
        if year% 100==0:
            if year%400==0:
                leapyear=True
            else:
                leapyear=False
        else:
            leapyear=True
    else:
        leapyear=False          

def daysinmonth(year,month):
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month>12 or month<1:
        return 0
    else:
        if leap_year(year) and month ==2:
            return 29
        else:
            return month_list[month]
    

year=int(input("\nEnter the Year : "))
month=int(input("Enter the month : "))
output=daysinmonth(year,month)
if output==0:
    print("Invalid Month")
else:
    print(f"There are {output} in {month}")