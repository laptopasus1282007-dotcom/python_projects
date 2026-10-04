#This is 9th project.
#Age calculator system 

from datetime import date 

birth_day = int(input("Enter Your Birth Date : "))
birth_month = int(input("Enter Your Birth Month : "))
birth_year = int(input("Enter Your Birth Year : "))

birth_date = date(birth_year,birth_month,birth_day)
today = date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0 :
    months -= 1
    if today.month == 1 :
        prev_month_days = 31

    else :
        prev_month = today .month - 1 
        prev_month_year = today.year
        import calendar
        prev_month_days = calendar .monthrange(prev_month_year,prev_month)[1]
    days += prev_month_days

    if months < 0 :
        years -= 1
        months += 12

    print(f"\nYour Age is : {years} years, {months} months, {days} days")

