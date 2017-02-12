# variables
infant = 0-1
child = 1-12
teenager = 13-19
adult = 20
# Decided to go with float instead of int.
# I Felt most little kids always wanna say "I am 5 and a half"
age = float(input(" Enter a persons age: "))
if age <= 1:
    print(" You are an infant! ")
elif age > 1 and age < 13:
    print("You are a child: ")
elif age < 13 and age < 20:
    print("You are a teenager: ")
elif age >= 20:
    print("You are an adult: ")
else:
    print("Invalid entry, please try again: ")
