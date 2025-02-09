class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    @property
    def get_side_length(self):
        return self.__side_length

    @get_side_length.setter
    def get_side_length(self, value):
        if type(value) is int and value > 0:
            self.__side_length = value
        else:
            if type(value) is not int:
                raise TypeError("Invalid type: value must be an integer")
            else:
                raise ValueError("Value must be a positive integer")

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        return f'Square side length:{self.__side_length}{Figure.unit}, area:{self.calculate_area()}{Figure.unit}'


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    @property
    def get_length(self):
        return self.__length

    @get_length.setter
    def get_length(self, value):
        if type(value) is int and value > 0:
            self.__length = value
        else:
            if type(value) is not int:
                raise TypeError("Invalid type: length must be an integer")
            else:
                raise ValueError("Length must be a positive integer")

    @property
    def get_width(self):
        return self.__width

    @get_width.setter
    def get_width(self, value):
        if type(value) is int and value > 0:
            self.__width = value
        else:
            if type(value) is not int:
                raise TypeError("Invalid type: width must be an integer")
            else:
                raise ValueError("Width must be a positive integer")

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        return (f'Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, '
                f'area: {self.__length * self.__width}')


kvadrat1 = Square(5)
# kvadrat1.side_length = -2 \\ строка для вызова ошибки ValueError в классе Square
kvadrat2 = Square(3)
rect1 = Rectangle(5, 10)
# rect1.get_length = 4.5 \\ строка для вызова ошибки TypeError в классе Rectangle
# rect1.get_width = -2 \\ строка для вызова ошибки ValueError в классе Rectangle
rect2 = Rectangle(10, 20)
rect3 = Rectangle(20, 30)

list_of_figures = [kvadrat1, kvadrat2, rect1, rect2, rect3]
for fig in list_of_figures:
    print(fig.info())
