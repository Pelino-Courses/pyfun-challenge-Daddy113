def process_operations(*args,**kwargs):
    """
    this function will help to make operation on operand given 
    
    """
    if not args:
        raise ValueError("No numbers provided.")
    for val in args:
        if not isinstance(val,(int,float)):
            raise ValueError(f"invalid number: {val}")
    result=args[0]
    numbers=args[1:]
    if kwargs.get("add"):
        for num in numbers:
            result+=num
    if kwargs.get("substract"):
        for num in numbers:
            result-=num
    if kwargs.get("multiply"):
        for num in numbers:
            result*=num                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    if kwargs.get("divide"):
        for num in numbers:
            if num==0:
                raise ZeroDivisionError("you can not divide by zero.")
            result/=num
    return result

def calculate(*args,**kwargs):
    try:
        return process_operations(*args,**kwargs)
    except Exception as e:
        return f"Error: {e}"   

if __name__=="__main__":
    print("Mathematical calculator")
    number_input =input("Enter numbers that are separated by commas(e.g: 10,6,54): ")
    try:
        numbers=[float(num.strip()) for num in number_input.split(",")] 
    except ValueError:
        print("Invalid input.Please enter only numbers.")
        exit() 

    print("\nchoose an operation:")
    print("1.Add")
    print("2.substract")
    print("3.Multiply")
    print("4.Divide")

    choice=input("Enter your choice (1-4): ").strip()
    if choice=="1":
        result=calculate(*numbers,add=True)
    elif choice=="2":
        result=calculate(*numbers,substract=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    elif choice=="3":
        result=calculate(*numbers,multiply=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    elif choice=="4":
        result=calculate(*numbers,divide=True)
    else:
        result="Error: Invalid operation selected."

    print(f"Result: {result}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   