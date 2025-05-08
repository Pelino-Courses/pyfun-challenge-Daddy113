import math
class Shape:
    """
    this is shape class
    """
    def area(self):
        """"
        this function is overriden by subclasses which is used to calculate area of a shape
        
        """
        raise NotImplementedError("The subclasses must override area()")
    
    def __str__(self):
        
        return "shape class"

class circle(Shape):
    """
    class of circle shape
    """
    def __init__(self,radius):
        if radius<=0:
            raise ValueError("Radius must be positive")
        self.radius=radius

    def area(self):
        return math.pi* self.radius**2
    
    def __str__(self):
        return f"circle with radius {self.radius}"
    
class rectangle(Shape):
    """"
    class of rectangle shape
    """
    def __init__(self,width,height):
        if width<=0 or height<=0:
            raise ValueError("Width and height must be positive")
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class triangle(Shape):
    """
    class of triangle shape 
    """
    def __init__(self,a,b,c):
        if a<=0 or b<=0 or c<=0:
            raise ValueError("sides must be positive")
        if a+b<=c or a+c<=b or b+c<=a:
            raise ValueError("Invalid triangle sides")
        
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        
        s=(self.a + self.b + self.c)/2

        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def __str__(self):
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"
    
def main():
    print("          welcome to Shape Area calculator\n")
    print("choose a shape to create: ")
    print("1.circle")
    print("2.Rectangle")
    print("3.Triangle") 

    choice=input("Enter the number of the shape from 1 to 3: ").strip() 

    try:
        if choice=="1":
            radius=float(input("Enter radius: "))
            shape=circle(radius)
        elif choice=="2":
            width=float(input("Enter width: "))
            height=float(input("Enter height: "))
            shape=rectangle(width,height)
        
        elif choice=="3":
            a=float(input("Enter side a: "))
            b=float(input("Enter side b: "))
            c=float(input("Enter side c: "))
            shape=triangle(a,b,c)
        else:
            print("Invalid choice.")
        print(shape)
        print(f"Area: {shape.area()}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__=="__main__":
        main()
    

        
