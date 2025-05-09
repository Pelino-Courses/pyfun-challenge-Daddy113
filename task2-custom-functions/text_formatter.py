def formatted_text(text,prefix="",suffix="",capitalize=False,max_length=None):
    """
    this function take the text and adds to it prefix,suffix and capitalize the text if needed by the user and give the certain length preffered by the user

    """
    if not isinstance(text,str) or not text.isalpha():
        raise TypeError("Text must be string that have only the letters as its characters.")
    if not isinstance(prefix,str) or not isinstance(suffix,str):
        raise TypeError("both prefix and suffix must be strings")
    if capitalize=="yes":
        text=text.capitalize()
    if prefix:
        text=prefix+text
    if suffix:
        text= text+suffix
    if  max_length and len(text)>max_length:
        text=text[:max_length]
        
    return text
def get_user_input():
    """
    this function help to get the text from the user to be formatted 

    """
    print("            $$$$$$$ welcome to the Text Formatter $$$$$$$")
    user_text=input("\nEnter the text to be formatted: ")
    if not user_text.isalpha():
        raise ValueError("Text must only have letters as it''s characters.")
    if input("Do you want to add a prefix to your text?(Answer:yes/no): ").lower().strip()=="yes":
        prefix=input("Enter the prefix: ")
    else:
    #     raise ValueError(" use the answer that are shown  please!!!")
        prefix=""

    
    if input("Do you want to add suffix on your text?(Answer:yes/no): ").lower().strip()=="yes":
        suffix=input("Enter the suffix: ")
    else:
    #     raise ValueError(" use the answer that are shown  please!!!")
        suffix=""

    capitalize=input("Do you want to capitalize the first letter?(Answer:yes if not leave it blank): ").lower()
    max_length=input("Enter the maximum length(Leave it blank if no limit needed): ")
    max_length=int(max_length) if max_length else None
    return user_text,prefix,suffix,capitalize,max_length
if __name__=="__main__":
    try:
        user_text,prefix,suffix,capitalize,max_length=get_user_input()
        formatted_text=formatted_text(user_text,prefix,suffix,capitalize,max_length)
        print(f"\n Formatted text:{formatted_text}")
    except(TypeError,ValueError) as e:
        print(f"Error:{e}")