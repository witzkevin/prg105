numberOfMonths = 0
inchesOfRain = 0
numberOfYears = int(input("Number of years "))

for currentYear in range(1, numberOfYears + 1):
    for currentMonth in range(1, 13):
        inchesRainPerMonth = float(input("Inches of rainfall for month " \
                + format( currentMonth, "d") + \
                ", year " + format(currentYear, "d") + " : "))
        inchesOfRain = inchesOfRain + inchesRainPerMonth
        numberOfMonths = numberOfMonths + 1

aveRain = inchesOfRain / numberOfMonths
print("Number of months:" + format( numberOfMonths, "d"),"total inches of rain: " + format( inchesOfRain, ".2f" ), \
"average rain:" + format(aveRain, ".2f"), sep="\n")
