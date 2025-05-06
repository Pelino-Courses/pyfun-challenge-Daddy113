from datetime import datetime

def datediff(date1,date2,format="%Y-%m-%d"):
    """
    this function help in finding the difference between two dates thaat are given by the user

    Args: 
     date1(str): The first date that is given by the user which must be a string 
     date2(str): The second date that is given by the user which must be a string 
     format(str): The  format which is dates are provided (default: "%Y-%m-%d" )

    
    """
    try:
        date1=datetime.strptime(date1,format)
        date2=datetime.strptime(date2,format)

        # we calculate the difference between our dates 
        diff=abs((date2-date1).days)
        return diff
    except ValueError:
        return "Invalid date format.please!!! use the correct format to write your dates"

def main():
    print("welcome to the calculator for date difference")
    while True:
        try:
            #the user input the dates to calculate their difference in days 
            date1=input("Enter the first date(use this format: YYYY-MM-DD): ").strip()
            date2=input("Enter the second date(use this format: YYYY-MM-DD): ").strip()
            # we give error message if dates are not all given 
                   
            if not date1 or not date2:
                print("Error: you have to enter both dates to calculate their difference")
            diff=datediff(date1,date2)
            if isinstance(diff,int):
                print(f"The difference between the two dates is :{diff} days.")
            # else:
            #     print(diff)
            break
        except Exception as e:
            print(f"An eror occured: {e}")
            break
main()