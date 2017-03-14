NUM_MONTHS = 12


def main():
    # creating a list to hold rain info
    rain = [0] * NUM_MONTHS

    # Get rainfall for each month
    for index in range(NUM_MONTHS):
        print("Enter the rainfall for month ", index + 1, ": ", sep="", end="")
        rain = float(input())
        values = [rain]

    ave_rain = rain / 12
    print("The average rain fall for the year is: ", ave_rain)

    my_list = [rain]
    print('The highest month of rain ', max(my_list))

    my_list = [rain]
    print('The lowest month of rain ', min(my_list))


main()
