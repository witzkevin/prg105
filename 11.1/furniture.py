class Furniture(object):
    def __init__(self, desk, chair, filing_cabinet):
        # Adding my mutators
        self.__desk = desk
        self.__chair = chair
        self.__price = price

        # Adding my getters and setters

        def get_desk(self):
            return self.__desk

        def get_chair(self):
            return self.__chair

        def get_price(self):
            return self.__price

        def get_item_price(self):
            return self.__price * self.quantity

        def __str__(self):
            line_item = self.__chair + " qty- " + str(self.__chair) + "each:  ${:0, .2f}".format(
                self.__price) + " total= ${:0,.2f}".format(self.get_item_price())
            return line_item


# initialize

desk = Furniture("Solid Oak", 1, 125)
desk2 = Furniture("Particle Board", 1, 75)
chair = Furniture("Leather", 1, 50)
chair2 = Furniture("Wood", 1, 35)
filing_cabinet = Furniture("Metal", 1, 70)
filing_cabinet2 = Furniture("Plastic", 1, 45)

print(desk)
print(desk2)
print(chair)
print(chair2)
print(filing_cabinet)
print(filing_cabinet2)
