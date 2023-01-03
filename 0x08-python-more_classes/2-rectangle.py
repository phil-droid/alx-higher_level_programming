#!usr/bin/python3
"""
Rectangle class based on rectangle 1
"""

Class Rectangle:

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """

        self.width = width
        self.height = height

    def width(self):
        """
        width getter
        """
        return self.__width

    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value
        
    def height(self):
        """
        height getter
        """
        return self.__height

    def height(self, value):
        """
        height setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """
        Returns area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns perimter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
    
