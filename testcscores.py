def ave():
    test_one = float(input("Enter test score 1: "))
    test_two = float(input("Enter test score 2: "))
    test_three = float(input("Enter test score 3: "))
    test_four = float(input("Enter test score 4: "))
    test_five = float(input("Enter test score 5: "))

    average = calc_average(test_one, test_two, test_three, test_four, test_five)
    print('The average of your five test scores is ', average)
    return average


def calc_average(t1, t2, t3, t4, t5):
    my_average = (t1 + t2 + t3 + t4 + t5)/5
    return my_average


def determine_grade(grade):
    # Getting the letter grade
    if grade >= 90:
        grade = "a"
    elif 80 <= grade <= 89:
        grade = "b"
    elif 70 <= grade <= 79:
        grade = "c"
    elif 60 <= grade <= 69:
        grade = "d"
    else:
        grade = "f"
    print("your letter grade is", grade)


def main():
    grade = ave()
    determine_grade(grade)


main()
