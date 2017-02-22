# Asking for all my monthly charges
def askForExspenses():
    loanPayment = float(input("Enter what your car loan payment is per month: "))
    insurance = float(input("Enter what your car insurance payment is per month: "))
    gas = float(input("Enter what your cars gas usage is per month: "))
    oil = float(input("Enter the cost of oil for your car per month: "))
    tires = float(input("Enter the cost of tires for your car per month: "))
    maintenance = float(input("Enter the cost of your cars maintenance per month: "))
    return loanPayment, insurance, gas, oil, tires, maintenance
# Tried to incorp this into my first funtion, got a little messy so I made another
# function to make it clean. (function is for gettting all monthly bills
def getTotalMonthlyBill( bill1, bill2, bill3, bill4, bill5, bill6):
    totalMonthlyBill = bill1 + bill2 + bill3 + bill4 + bill5 + bill6
    return totalMonthlyBill

# simply getting yearly cost.
def getYearlyCost(totalMonthlyBill):
    yearlyCost = totalMonthlyBill * 12
    return yearlyCost
# Using this parameter to the print command to show the total costs.
def printDetails(totalMonthlyBill, yearlyCost):
    print("Your total monthly auto cost is $" , format(totalMonthlyBill, ".2f"), "and your yearly auto cost is $",\
    format(yearlyCost, ",.2f"))
# Running the whole function as one here. Last step.
def main():
    loanPayment, insurance, gas, oil, tires, maintenance = askForExspenses()

    totalMonthlyBill = getTotalMonthlyBill(loanPayment, insurance, gas, oil, tires, maintenance)

    yearlyCost = getYearlyCost(totalMonthlyBill)
    printDetails(totalMonthlyBill, yearlyCost)
main()
