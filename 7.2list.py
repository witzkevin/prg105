import random

MAX_DIGITS = 20
START = 0
END = 101


# Main function

def main():
    numbers = [0] * 20

    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)

        print("Here is a random 20 numbers: ")
        for index in range(MAX_DIGITS):
            print(numbers[index], end="")
        user()
        print()


def user():
    user_number = int(input(" Enter a number 1-100: "))
    print(user_number)


main()
