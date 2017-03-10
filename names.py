file = open("names.txt", "r")
count = 0

for line in file:
    print(line)
    count += 1

print("There were " + str(count) + " names ")
file.close()
