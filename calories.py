FAT_GRAMS = 9
CARB_GRAMS = 4
PROTEIN_GRAMS = 4


def main():
    fat_calories = fat()
    protein_calories = protein()
    carb_calories = carb()
    sum(fat_calories, protein_calories, carb_calories)


def fat():
    f_grams = float(input("Enter the number of fat grams: "))
    calories_from_fat = f_grams * FAT_GRAMS
    print(calories_from_fat, "calories are from fat  ")
    return calories_from_fat


def carb():
    c_grams = float(input("Enter the number of carb grams: "))
    calories_from_carbs = c_grams * CARB_GRAMS
    print(calories_from_carbs, "calories are from carb  ")
    return calories_from_carbs


def protein():
    p_grams = float(input("Enter the number of protein grams: "))
    calories_from_protein = p_grams * PROTEIN_GRAMS
    print(calories_from_protein, "calories are from protein  ")
    return calories_from_protein


def sum(calories_from_fat, calories_from_carbs, calories_from_protein):
    result = (calories_from_fat + calories_from_carbs + calories_from_protein)
    print(result, "total calories are from fat, protein, and carbs ")
    return calories_from_fat


main()
