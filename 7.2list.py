import random

COUNT = 20


def main():
    # setting my list of 20 and getting random numbers set
    random_list = [0] * 20
    index = 0
    while index < COUNT:
        random_list[index] = random.randint(1, 100)
        index += 1

    guess = entry()
    greater_than(random_list, guess)


def entry():
    # setting my loop
    valid = False
    while not valid:
        try:
            print("Enter a number 1 through 100: ")
            user_guess = int(input())
            if 0 < user_guess < 101:
                valid = True
                return user_guess
            else:
                print("Your number must be between 1 and 100. ")
        except ValueError:
            print("You need a valid number. ")


def greater_than(rand_list, guess):
    # Printing their guess with the list
    for item in rand_list:
        if item > guess:
            print(item)
    if max(rand_list) < guess:
        print("There are no numbers in the list greater than your number. ")


main()
