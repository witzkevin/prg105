import pickle

# My global constants
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# My main menu
def main():
    try:
        input_file = open("customer_file.dat", "rb")
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("File is not found, add a new customer")
        customers = {}

    choice = 0

    while choice != QUIT:
        choice = menu()

        # processing the choice
        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


# Showing the main menu
def menu():
    print()
    print("Customers phone lookup")
    print("----------------------")
    print("1.  Look up customer")
    print("2.  Add new customer")
    print("3. Change a email")
    print("4.  Delete a customer")
    print("5  Quit the program\n")
    # Getting the choice from user

    choice = int(input("Enter the number of your choice:  "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice please:  "))
    return choice


# Looking up a customer
def look_up(customers):
    name = input("Enter a customers name: ")
    print(customers.get(name, "Not Found"))


# Adding a new customer
def add(customers):
    name = input("Enter a customers name: ")
    phone = input("Enter a customers email: ")
    if name not in customers:
        customers[name] = phone
    else:
        print("That entry already exists: ")


# Changing an Email
def change(customers):
    name = input("Enter a customers name: ")
    if name in customers:
        phone = input("Enter the new email: ")
        customers[name] = phone
    else:
        print("That customer is not found: ")


# Deleting a customer
def delete(customers):
    name = input("Enter the customers name : ")
    if name in customers:
        del customers[name]
    else:
        print("That customer is not found here: ")


# Saving the data
def save(customers):
    print("The data file has been updated with all the new changes: ")
    save_file = open("customer_file.dat", "wb")
    pickle.dump(customers, save_file)
    save_file.close()


main()
