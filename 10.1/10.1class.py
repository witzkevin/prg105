# This program will pickle the personal information
import pickle


# Constant for file name
FILENAME = "personal.dat"


def main():
    # Initialize a variable to control the loop.
    again = "y"

    # Open the file
    output_file = open(FILENAME, "wb")

    # Getting data from user
    while again.lower() == "y":
        # Getting the personal data
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        age = input("Enter your age: ")
        phone = input("Enter your phone number: ")

        # Creating a personal database object
        information = personal.Personal(name, address, age, phone)

        # Pickle the object
        pickle.dump(information, output_file)


        # Get more info
        again = input("Enter more data?   (y/n): ")


    # Close the file
    output_file.close()
    print("All info was written to ", FILENAME)


main()
