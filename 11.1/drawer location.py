import furniture


def main():
    # implementing the furiture class

    chair = furniture.Furniture("chair", "wood", "24 inches", "24 inches", "28 inches", "$59.99")
    print(chair)

    print("\n\n\n")

    desk = furniture.Desk("Desk", "Wood", "82 inches", "64 inches", "48 inches", "$485.99", "left", "2")
    print(desk)


main()
