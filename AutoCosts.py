def ask_for_expenses():  # Asking for all my monthly charges
    loan_payment = float(input("Enter what your car loan payment is per month: "))
    insurance = float(input("Enter what your car insurance payment is per month: "))
    gas = float(input("Enter what your cars gas usage is per month: "))
    oil = float(input("Enter the cost of oil for your car per month: "))
    tires = float(input("Enter the cost of tires for your car per month: "))
    maintenance = float(input("Enter the cost of your cars maintenance per month: "))
    return loan_payment, insurance, gas, oil, tires, maintenance


def get_total_monthly_bill(bill1, bill2, bill3, bill4, bill5, bill6):
    total_monthly_bill = bill1 + bill2 + bill3 + bill4 + bill5 + bill6
    return total_monthly_bill  # Tried to incorporate this into my first function, got a little messy so I made another


# function to make it clean. (function is for getting all monthly bills

def get_yearly_cost(total_monthly_bill):  # Simply getting yearly cost.
    yearly_cost = total_monthly_bill * 12
    return yearly_cost


def print_details(total_monthly_bill,
                  yearly_cost):  # Using this parameter to the print command to show the total costs.
    print("Your total monthly auto cost is $", format(total_monthly_bill, ".2f"), "and your yearly auto cost is $",
          format(yearly_cost, ",.2f"))


def main():
    loan_payment, insurance, gas, oil, tires, maintenance = ask_for_expenses()
    # Running the whole function as one here. Last step.
    total_monthly_bill = get_total_monthly_bill(loan_payment, insurance, gas, oil, tires, maintenance)

    yearly_cost = get_yearly_cost(total_monthly_bill)
    print_details(total_monthly_bill, yearly_cost)


main()
