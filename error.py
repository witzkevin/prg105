def main():
    # open files for reading
    filename = input("Enter file name: ")
    infile = open(filename, "r")

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    num4 = int(infile.readline())
    num5 = int(infile.readline())
    num6 = int(infile.readline())
    num7 = int(infile.readline())
    num8 = int(infile.readline())
    num9 = int(infile.readline())
    num10 = int(infile.readline())
    num11 = int(infile.readline())
    num12 = int(infile.readline())
    num13 = int(infile.readline())
    num14 = int(infile.readline())
    num15 = int(infile.readline())
    num16 = int(infile.readline())
    num17 = int(infile.readline())
    num18 = int(infile.readline())


    # adding them up
    average = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14
               + num15 + num17 + num18) / 18


    for line in infile:
        amount = float(line)
        average += amount

    # closing the file
    infile.close()

    # displaying all numbers and average
    print("The numbers are: ", num1, num2, num3, num3, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14,
          num15, num16, num17, num18)
    print("The average of these numbers are: ", format(average, ",.2f"))

    except IOError:
         print("An error occured trying to read this file")

    except ValueError:
        print("Non-numeric data found in the file")


 # call the main function
main()
