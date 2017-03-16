def search():
    boyname = str(input("Enter a boys name: "))
    girlname = str(input("Enter a girls name: "))

    boys_names = []
    girls_name = []

    f1 = open("BoyNames.txt", "r")

    for names in f1.readlines():
    names = names.strip("\n")
    boys_names.append(names)
    f1.close()

    f2= open("GirlNames.txt", "r")
    names = names.strip("\n")
    f1.close()

    except:
           print("BoyNames.txt file is not present.")



search()
