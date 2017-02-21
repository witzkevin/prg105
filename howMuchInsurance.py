# Getting the value for the replacement for step 1
def askForBuildingReplacement():
    buildingReplacement = float(input("Enter the replacement cost of the building: "))

    return buildingReplacement

# Here I am taking my original building cost and finding
# how much I should insure it for.
def findMinimumInsurance(buildingReplacement):
    minimumInsurance = (80 / 100) * buildingReplacement
    return minimumInsurance

# Here I am passing a parameter function and printing how much to insure for
def printDetails(buildingReplacement, minimumInsurance):
    print("You should insure your house for $", format(minimumInsurance, ",.2f"))

# Here is where it all comes together.
def main():
    buildingReplacement = askForBuildingReplacement()
    minimumInsurance = findMinimumInsurance(buildingReplacement)
    printDetails(buildingReplacement, minimumInsurance)

main()
