from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate = "1995-05-15" 
date = "2026-01-02"

def age(birthdate, date):

    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    date = datetime.strptime(date, '%Y-%m-%d')

    diff = relativedelta(date, birthdate)
    print(f'Age is {diff.years} years, {diff.months} months, and {diff.days} days')

age(birthdate, date)