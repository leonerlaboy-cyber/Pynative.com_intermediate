employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]

new = sorted(employees, key=lambda x: x['salary'], reverse=True)

print(new)