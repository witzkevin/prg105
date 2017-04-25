class Furniture(object):
    # initializing variables

    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

        # Adding my getters and setters

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    # Accessors

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        return "Category: " + self.__category + \
            "\nMaterial: " + self.__material + \
               "\nLength: " + self.__length + \
               "\nWidth: " + self.__width + \
               "\nHeight: " + self.__height + \
               "\nPrice: " + self.__price


class Desk(Furniture):
    # call super class
    def __init__(self, category, material, length, width, height, price, drawer_location, num_drawers):
        Furniture.__init__(self, category, material, length, width, height, price)

        # adding new

        self.__drawer_location = drawer_location
        self.__num_drawers = num_drawers

    # mutators
    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def set_num_drawers(self, num_drawers):
        self.__num_drawers = num_drawers

    # accessors
    def get_drawer_location(self):
        return self.__drawer_location

    def get_num_drawers(self):
        return self.__num_drawers

    def __str__(self):
        return "Catergory: " + self.get_category() + \
            "\nMaterial: " + self.get_material() + \
               "\nLength: " + self.get_length() + \
               "\nWidth: " + self.get_width() + \
               "\nHeight: " + self.get_height() + \
               "\nPrice: " + self.get_price() + \
               "\nDrawer Location: " + self.__drawer_location + \
               "\nNumber of Drawers: " + self.__num_drawers
