from datetime import timedelta, datetime

def add_business_days(start_date, n):
    current_date = start_date
    days_added = 0
    
    while days_added < n:
        current_date += timedelta(days=1)
        
        if current_date.weekday() < 5:
            days_added += 1
            
    return current_date

# Usage
start = datetime(2026, 1, 2) # A Friday
result = add_business_days(start, 5)
print(f"Start: {start.strftime('%A, %Y-%m-%d')}")
print(f"Business Target: {result.strftime('%A, %Y-%m-%d')}")