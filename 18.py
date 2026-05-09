from datetime import datetime
from dateutil.relativedelta import relativedelta

def next_new_year(date):

    # date = datetime.strptime(date, '%Y-%m-%d')
    # print(date)

    next_year = date.year + 1
    # print(next_year)
    next_ny = datetime(next_year, 1, 1, 0, 0, 0)
    # print(next_ny)

    # diff = relativedelta(next_ny, date)
    diff = next_ny - date
    

    print(diff)
    print(f'{diff.days} days, {diff.seconds // 3600} hours, {(diff.seconds % 3600) // 60} minutes till the New Year!')

# next_new_year("2026-01-02")
now = datetime.now()
print(now)
next_new_year(now)