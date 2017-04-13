import question


def main():
    q1 = question.Question("What is the color of the sun? ", "A. Red", "B. Blue", "C. Yellow", "D. Taco", "C")
    q2 = question.Question("What shape is the earth? ", "A. Round", "B. Square", "C. Flat", "D. Octagon", "A")
    q3 = question.Question("Who is the current president? ", "A. Obama", "B. Clinton", "C. Trump", "D. Witz", "C")
    q4 = question.Question("What town is MCC in? ", "A. Crystal Lake", "B. McHenry", "C. Algonquin", "D. Flint", "A")
    q5 = question.Question("What is the current year? ", "A. 1999", "B. 2017", "C. 2016", "D. 320AD", "B")
    q6 = question.Question("What color is a chocolate lab? ", "A. Brown", "B. Blue", "C. Yellow", "D. Black", "A")
    q7 = question.Question("Who won the 2016 MLB World Series? ", "A. Bears", "B. Black hawks", "C. White sox",
                           "D. Cubs", "D")
    q8 = question.Question("What color is grass? ", "A. Red", "B. Blue", "C. Yellow", "D. Green", "D")
    q9 = question.Question("Who is on the dollar bill? ", "A. Lincoln", "B. Washington", "C. Bush", "D. You", "B")
    q10 = question.Question("Is it okay to eat the shell of a kiwi? ", "A. Yes", "B. No", "C. maybe", "D. Eww", "A")

    player1 = 0  # Holding the score
    player2 = 0  # Holding the score

    set_1 = [q1, q2, q3, q4, q5]

    set_2 = [q6, q7, q8, q9, q10]

    print("player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        print(query.get_a5())
        guess = input("Enter the letter of your choice: ")
        if guess.upper() == query.get_answer():
            print("You are correct: ")
            player1 += 1

    print("Player 1 earned: " + str(player1) + "points.")

    print("player 2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a6())
        print(query.get_a7())
        print(query.get_a8())
        print(query.get_a9())
        print(query.get_a10())
        guess = input("Enter the letter of your choice: ")
        if guess.upper() == query.get_answer():
            print("You are correct: ")
            player2 += 1

    print("Player 2 earned: " + str(player1) + "points.")

    if player1 > player2():
        print("Player 1 is the winner!! ")
    else:
        print("PLayer 2 is the winner!! ")
main()
