import math

class Shape:
    """
    Abstract base class for geometric shapes. This class provides the structure for calculating the area
    and displaying the shape. Subclasses must implement the area() method.
    """
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        
        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("Subclasses must override area() method")
    
    def __str__(self):
        """
        Returns a string representation of the shape. This method can be overridden by subclasses 
        to provide more specific details about the shape.
        
        Returns:
            str: A generic string representation of the shape.
        """
        return "Generic shape"


class Circle(Shape):
    """
    Represents a circle with a given radius. Inherits from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a new Circle instance with a specified radius.
        
        Args:
            radius (float): The radius of the circle. Must be positive.
        
        Raises:
            ValueError: If the radius is less than or equal to zero.
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        """
        Calculates the area of the circle using the formula π * radius^2.
        
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2
    
    def __str__(self):
        """
        Returns a string representation of the circle.
        
        Returns:
            str: A string describing the circle with its radius.
        """
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    """
    Represents a rectangle with a given width and height. Inherits from Shape.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with a specified width and height.
        
        Args:
            width (float): The width of the rectangle. Must be positive.
            height (float): The height of the rectangle. Must be positive.
        
        Raises:
            ValueError: If the width or height is less than or equal to zero.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculates the area of the rectangle using the formula width * height.
        
        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height
    
    def __str__(self):
        """
        Returns a string representation of the rectangle.
        
        Returns:
            str: A string describing the rectangle with its width and height.
        """
        return f"Rectangle with width {self.width} and height {self.height}"


class Triangle(Shape):
    """
    Represents a triangle with three sides (a, b, c). Inherits from Shape.
    """
    def __init__(self, a, b, c):
        """
        Initializes a new Triangle instance with three side lengths.
        
        Args:
            a (float): The length of side a. Must be positive.
            b (float): The length of side b. Must be positive.
            c (float): The length of side c. Must be positive.
        
        Raises:
            ValueError: If any of the sides are less than or equal to zero.
            ValueError: If the sides do not form a valid triangle.
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        """
        Calculates the area of the triangle using Heron's formula:
        Area = √(s * (s - a) * (s - b) * (s - c)), where s is the semi-perimeter.
        
        Returns:
            float: The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def __str__(self):
        """
        Returns a string representation of the triangle.
        
        Returns:
            str: A string describing the triangle with its three sides.
        """
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"


def main():
    """
    Prompts the user to choose a shape to create and calculates its area.
    Based on the user's input, it instantiates one of the Shape subclasses
    (Circle, Rectangle, or Triangle) and prints the shape's details and area.
    """
    print("Choose a shape to create:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter the number of the shape: ").strip()

    try:
        if choice == '1':
            radius = float(input("Enter radius: "))
            shape = Circle(radius)
        elif choice == '2':
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shape = Rectangle(width, height)
        elif choice == '3':
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            shape = Triangle(a, b, c)
        else:
            print("Invalid choice.")
            return

        print(shape)
        print(f"Area: {shape.area():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
