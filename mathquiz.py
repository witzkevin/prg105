import random

number_one = random.randint(1, 999)
number_two = random.randint(1, 999)


def question():  # I am inputting the users answer to see if it is correct
    global number_one
    global number_two

    user_answer = int(input("what is " + str(number_one) + ' + ' + str(number_two)))
    return user_answer


def check_answer(user_answer):  # Here is where I determine if they are right
    # If so, they get a message, if not they get the right answer
    global number_one
    global number_two

    right_answer = number_one + number_two
    if user_answer == right_answer:
        print("You got it right!")
    else:
        print("Wrong, the right answer is", right_answer)


def main():  # running the main program
    user_answer = question()
    check_answer(user_answer)


main()
