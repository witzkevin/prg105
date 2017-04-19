class drawer_location(desk):


    def __init__(self, desk, chair, filing_cabinet,left_drawers, right_drawers, both_side ):

        # Call the parent class

        Furniture.__init(self, desk, chair, filing_cabinet)

        self.__left_drawers = left_drawers
        self.__right_drawers = right_drawers
        self.__both_side = both_side

    # Add the mutator
    def set_left_drawers(self, left_drawers):
        self.__left_drawers = left_drawers

    def set_right_drawers(self, right_drawers):
        self.__right_drawers = right_drawers

    def set_both_side(self, both_side):
        self.__both_side = both_side

    # adding the accessor for drawer sides

    def get_left_drawers(self):
        return self.__left_drawers


    def get_right_drawers(self):
        return self.__right_drawers


    def get_both_side(self):
        return self.__both_side

left_side_drawer = Drawer_Location("Drawer Locations," 1, 25, "Left Side Drawer")
right_side_drawer = Drawer_Location("Drawer Locations," 1, 25, "Right Side Drawer")
both_side_drawer = Drawer_Location("Drawer Locations," 1, 45, "Both Side Drawer")
print (left_side_drawer)
print (right_side_drawer)
print (both_side_drawer)




