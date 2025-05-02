from datetime import datetime

def dates_difference(date1, date2, format="%Y-%m-%d"):
    """
    Calculates the difference in days between two dates that are provided by the user.

    Args:
        date1 (str): The first date must be string.
        date2 (str): The second date must be string.
        format (str): The format in which the dates are provided and the  Default format  is "%Y-%m-%d".

    Returns:
        int: The number od day or days would be integer .

    Raises:
        ValueError: If the date strings do not match any of the expected format in our program 

    Examples:
         format (YYYY-MM-DD):
             dates_difference("2025-05-01", "2025-05-10")
            

         format (DD/MM/YYYY):
             dates_difference("01/05/2025", "10/05/2025", "%d/%m/%Y")
            

        format (MM-DD-YYYY):
            dates_difference("05-01-2025", "05-10-2025", "%m-%d-%Y")  
    """
    try:
        date1 = datetime.strptime(date1, format).date()
        date2 = datetime.strptime(date2, format).date()
        return abs((date2 - date1).days)
    except ValueError:
        raise ValueError("Invalid date format. Please enter dates that match the format you have selected .")

if __name__ == '__main__':
    print("program to Calculate the difference in days between two dates.")
    # here there is options of formats that the user can choose from 
    format_options = {
        "1": ("%Y-%m-%d", "2025-05-02"),    
        "2": ("%d/%m/%Y", "02/05/2025"),    
        "3": ("%m-%d-%Y", "05-02-2025")     
    }
    print("\nSelect a date format:")
    for key, (fmt, example) in format_options.items():
        print(f"{key}. {fmt}  (e.g., {example})")
    selected_option = input("Enter your choice [1-3]: ").strip()
    format = format_options.get(selected_option, format_options["1"])[0]  # the default format is option 1
    # our user can input the data to use in our program 
    date1 = input(f"Enter the first date (format {format}): ")
    date2 = input(f"Enter the second date (format {format}): ")
    try:
        difference = dates_difference(date1, date2, format)
        print(f"The difference between {date1} and {date2} is: {difference} days")
    except ValueError as e:
        print(f"Error: {e}")
