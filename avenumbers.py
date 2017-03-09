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
