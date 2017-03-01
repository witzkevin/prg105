def ave():
    test_one = float(input("Enter test score 1: "))
    test_two = float(input("Enter test score 2: "))
    test_three = float(input("Enter test score 3: "))
    test_four = float(input("Enter test score 4: "))
    test_five = float(input("Enter test score 5: "))

    calc_average = (test_one + test_two + test_three + test_four + test_five) / 5
    print("The average of your five test scores are", calc_average)

    return test_one, test_two, test_three, test_four, test_five


def determine_grade(grade):
    # Getting the letter grade
    if grade >= 90:
        grade = "a"
    elif grade <= 89 and grade >= 80:
        grade = "b"
    elif grade <= 79 and grade >= 70:
        grade = "c"
    elif grade <= 69 and grade >= 60:
        grade = "d"
    else:
        grade = "f"
    print("your letter grade is", grade)


def main():
    grade = ave()
    determine_grade(grade)


main()
