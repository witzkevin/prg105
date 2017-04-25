import employee


# implementing the Production class

def main():
    emp_name = input(" Enter the employees name: ")
    emp_num = input(" Enter the employees number: ")
    emp_shift = input(" Enter the employees shift: ")
    emp_pay = input(" Enter the employees pay: ")
    emp = employee.ProductionWorker(emp_name, emp_num, emp_shift, emp_pay)

    print("Employee Name: " + emp.get_name())
    print("Employee Number: " + emp.get_number())
    print("Employee Shift: " + str(emp.get_shift()))
    print("Employee Pay Rate:  $" + str(emp.get_name()))

main()
