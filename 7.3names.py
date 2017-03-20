def main():
    f1 = open("BoyNames.txt", "r")
    f2 = open("GirlNames.txt","r")
    boys_names = f1.readlines()
    girls_names = f2.readlines()

    name = str(input("Enter a name: ")) + "\n"

    if name in boys_names:
        print("This is one of the popular boys name.")
    elif name in girls_names:
        print("This is one of the popular girl names")
    else:
        print("This is not one of the popular names")

main()
