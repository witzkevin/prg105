daysWorked = int(input("Number of days worked "))
dailyPay = .01
total = 0
print("day\tsalary")
for today in range(daysWorked):
    dailyPennies = 2 ** today
    total = total + dailyPennies
    print(today + 1, "\t", dailyPennies)

pay = total * dailyPay
print("\n pay:", pay,)
