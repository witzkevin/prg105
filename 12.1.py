def main():
    numbers = int(input('Enter a number: '))
    mysum = sum_num(numbers, 1)


def sum_num(numbers, mysum):
    start = 1
    end = numbers
    if start > end:
        return 0
    else:
        return mysum


main()
