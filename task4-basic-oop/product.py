class Product:
    """
    A class to represent a product in an inventory system.

    Attributes:
        name (str): The name of the product.
        price (float): The price per unit of the product. Must be non-negative.
        quantity (int): The quantity of the product in stock. Must be non-negative.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance with the given name, price, and quantity.

        Args:
            name (str): Name of the product.
            price (float): Price per unit of the product.
            quantity (int): Initial quantity in stock.

        Raises:
            ValueError: If price or quantity is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount: int):
        """
        Adds the specified amount to the product's inventory.

        Args:
            amount (int): The number of units to add.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
        """
        Removes the specified amount from the product's inventory.

        Args:
            amount (int): The number of units to remove.

        Raises:
            ValueError: If amount is negative or more than available quantity.
        """
        if amount < 0:
            raise ValueError("Amount to remove cannot be negative.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount

    def total_value(self) -> float:
        """
        Calculates the total value of the inventory for this product.

        Returns:
            float: Total value of the product's stock (price * quantity).
        """
        return self.price * self.quantity

    def display_info(self):
        """
        Prints detailed information about the product, including name,
        price, quantity, and total value.
        """
        print(f"\nProduct: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")


def list_products(products):
    """
    Displays a list of all available products with index numbers.

    Args:
        products (list of Product): The list of products in inventory.
    """
    if not products:
        print("No products available.")
        return
    print("\nAvailable Products:")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.name}")


def select_product(products):
    """
    Prompts the user to select a product by number from the list.

    Args:
        products (list of Product): The list of products.

    Returns:
        Product: The selected product instance, or None if invalid input.
    """
    list_products(products)
    if not products:
        return None
    try:
        choice = int(input("Select a product by number: "))
        if 1 <= choice <= len(products):
            return products[choice - 1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    """
    Runs the inventory management system with a menu-driven interface
    for adding products, viewing products, and modifying inventory.
    """
    products = []

    while True:
        print("\n=== Inventory Management Menu ===")
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Select Product and View Info")
        print("4. Add Inventory to Product")
        print("5. Remove Inventory from Product")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                product = Product(name, price, quantity)
                products.append(product)
                print("Product added successfully!")

            elif choice == "2":
                list_products(products)

            elif choice == "3":
                product = select_product(products)
                if product:
                    product.display_info()

            elif choice == "4":
                product = select_product(products)
                if product:
                    amount = int(input("Enter amount to add: "))
                    product.add_inventory(amount)
                    print("Inventory added successfully!")

            elif choice == "5":
                product = select_product(products)
                if product:
                    amount = int(input("Enter amount to remove: "))
                    product.remove_inventory(amount)
                    print("Inventory removed successfully!")

            elif choice == "6":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
