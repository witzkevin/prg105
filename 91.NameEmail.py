import pickle


def main():
    again = "y"  # controlling loop repetition.

    output_file = open("info.dat", "wb")

    while again.lower() == "y":
        save_data(output_file)

        again = input("Enter more data?  (y/n): ")

    output_file.close()


def save_data(file):
    person = {"name": input("Name: "), "email": input("Email: ")}

    pickle.dump(person, file)


main()
