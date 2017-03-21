# Write a program that lets the user enter a string and
#  displays the character that appears most frequently in the string.
def main():
    # Set my variable and an empty list
    my_string = input('Enter your string and I will count the letters:')

    counts = {}

    for letter in my_string:
        counts[letter] = counts.get(letter, 0) + 1

    print("The most frequent letter from most to least is: ", counts)


main()
