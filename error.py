def main():
    # open files for reading
    total = 0  # this will accumulate the total
    count = 0  # holds the count of the file
    infile = open("numbers.txt", "r")
    for num in infile:
        total += int(num)
        count += 1

    average = total / count
    # closing the file
    infile.close()

    print("The average of these numbers are: ", format(average, ",.2f"))


# call the main function
main()

while True:
    try:
        x = int(input("Please enter a number: "))

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

while True:
    try:
        x = int(input("Please enter a number: "))

    except IOError:
        print("Oops!  That was no valid number.  Try again...")


        # call the main function
main()
