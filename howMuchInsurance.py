def ask_for_building_replacement():  # Getting the value for the replacement for step 1
    building_replacement = float(input("Enter the replacement cost of the building: "))

    return building_replacement


def find_minimum_insurance(building_replacement):  #
    # Here I am taking my original building cost and finding
    # how much I should insure it for.
    minimum_insurance = (80 / 100) * building_replacement
    return minimum_insurance


def print_details(minimum_insurance):
    # Here I am passing a parameter function and printing how much to insure for

    print("You should insure your house for $", format(minimum_insurance, ",.2f"))


def main():
    # Here is where it all comes together.
    building_replacement = ask_for_building_replacement()
    minimum_insurance = find_minimum_insurance(building_replacement)
    print_details(minimum_insurance)


main()
