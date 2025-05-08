class Product:
    """
    A class to represent a product in an inventory system
    """
    def __init__(self,name,price,quantity):
        
        if price<0:
            raise ValueError("price can not be negative.")
        if quantity<0:
            raise ValueError("quantity can not be negative")
        self.name=name
        self.price=price
        self.quantity=quantity

    def add_inventory(self,amount):
        """
        function to add amount in our inventory 
        """
        if amount<0:
            raise ValueError("Amount to add can not be negative.")
        self.quantity+=amount

    def remove_inventory(self,amount):
        """
        function to remove amount in our inventory 
        """
        if amount<0:
            raise ValueError("Amount to remove can not be negative.")
        self.quantity-=amount

    def total_value(self):
        """
        function to calculate the total value of the product in inventory
        """
        return self.price*self.quantity

    def display_info(self):
        """
        function to display information about the product in the inventory
        """
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total value: ${self.total_value()}")
    
    def increase(self,amount):
        """
        this function help to increase price of product in inventory
        """
        if amount<0:
            raise ValueError("Amount to remove can not be negative.")
        self.price+=amount
    
    def decrease(self,amount):
        """
        this function help to Decrease price of product in inventory
        """
        if amount<0:
            raise ValueError("Amount to remove can not be negative.")
        self.price-=amount

def list_products(products):
    """
    function that shows all products we have in the inventory
    """
    if not products:
        print("No products available.")
        
    print("The product list:")
    for index,product in enumerate(products):
        print(f"{index+1}.{product.name}")

def select_product(products):
    """
    this function help to select product that the user what to get its information
    (it help to select that product the euser what to get its information)
    """
    list_products(products)
    if not products:
        return None
    try:
        choice=int(input("select a product by number: "))
        if 1<=choice<=len(products):
            return products[choice-1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("In valid input.please enter the number.")
        return None
    
def main():
    products=[]

    while True:
        print("             Inventory Management System\n")
        print("1.Add New product in Inventory")
        print("2.View all products in Inventory")
        print("3.Select product and view it's information")
        print("4.Increase product quantity in inventory")
        print("5.Decrease product quantity in inventory")
        print("6.Delete product from inventory")
        print("7.Increase the price of product")
        print("8.Decrease the price of product")
        print("9.Exit")

        choice=input("Enter your choice (1-6): ")
        try:
            if choice=="1":
                name=input("Enter product name: ")
                price=float(input("Enter product price: "))
                quantity=int(input("Enter product quantity: "))
                product=Product(name,price,quantity)
                products.append(product)
                print("\nproduct added successfully!!.\n")
            elif choice=="2":
                list_products(products)
                
            elif choice=="3":
                product=select_product(products)
                if product:
                    product.display_info()
                
            elif choice=="4":
                product=select_product(products)
                if product:
                    amount=int(input("Enter amount to add: "))
                    product.add_inventory(amount)
                    print("quantity added successfully!!")
            
            elif choice=="5":
                product=select_product(products)
                if product:
                    amount=int(input("Enter amount to remove: "))
                    product.remove_inventory(amount)
                    print("quantity removed successfully!!")
            elif choice=="6":
                product=select_product(products)
                if product:
                    products.remove(product)
                    print("Product removed ")

            elif choice=="7":
                product=select_product(products)
                if product:
                    amount=int(input("Enter amount to add: "))
                    product.increase(amount)
                    print("price changed successfully!!")
                
            elif choice=="8":
                product=select_product(products)
                if product:
                    amount=int(input("Enter amount to remove: "))
                    product.decrease(amount)
                    print("price changed successfully!!")

            elif choice=="9":
                print("Exiting program.Goodbye!!")
                exit()

            else:
                print("Invalid choice.please enter a number between 1 - 6.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__=="__main__":
    main()


