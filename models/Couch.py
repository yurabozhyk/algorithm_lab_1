class Couch():

    def __init__(self, width, length, color, brand):
        self.width = width
        self.length = length
        self.color = color
        self.brand = brand

    def __str__(self):
        return str(self.width) + ' '\
                + str(self.length) + ' '\
                + self.color + ' '\
                + self.brand
