raw_hours = input('Enter Hours\n')
raw_rate = input("Enter Rate\n")
hours = int(raw_hours)
rate=int(raw_rate)
if hours > 40:
    pay = 40 * rate
    overtime = hours - 40
    overtime_pay = overtime * rate * 1.5
    print("your salary is", pay + overtime_pay)
else:
    pay = hours * rate
    print("your salary is", pay)
