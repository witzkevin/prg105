def get_value(): # Asked user to for value of home and set a variable up
    value = float(input("What is the actual value of your property? "))
    calculate(value)


def calculate(my_value): # Here is where the math calculations take place.
    print("The county assessment value is: $", format((my_value * .60), ",.2f"))
    assessment_value = my_value * .6
    print("The final tax for the acre assessment is: $ ", format((assessment_value * .0072), ",.2f"))

get_value() # running the final program
