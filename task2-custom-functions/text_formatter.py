def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Formats the given text by optionally adding a prefix and/or suffix, capitalizing the result,
    and trimming it to a maximum length if specified.

    Parameters:
        text (str): The main text to be formatted. This must be a string containing only alphabetic characters.
        prefix (str): A string to be added at the beginning of the text. (Default: "")
        suffix (str): A string to be added at the end of the text. (Default: "")
        capitalize (bool): If True, capitalizes the first character of the text. (Default: False)
        max_length (int or None): If specified, trims the final string to this maximum length. If None, no trimming is done. (Default: None)

    Returns:
        str: The formatted string with the prefix, text, suffix, and any capitalization and length adjustments applied.

    Raises:
        TypeError: If `text`, `prefix`, or `suffix` are not strings, or if `text` contains non-alphabetic characters.
        ValueError: If `max_length` is not a valid integer.

    Examples:
         format_text("hello", prefix=">>", suffix="<<", capitalize=True)
        '>>Hello<<'

         format_text("sample text", max_length=10)
        'sample tex'

         format_text("example", capitalize=True)
        'Example'

         format_text("test", prefix="(", suffix=")", max_length=6)
        '(test)'

         format_text("trim this text", max_length=5)
        'trim'
    """
    # Ensure the text is a valid string and contains only alphabetic characters
    if not isinstance(text, str) or not text.isalpha():
        raise TypeError("Text must be a string containing only alphabetic characters.")

    # Ensure prefix and suffix are strings
    if not isinstance(prefix, str):
        raise TypeError("Prefix must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("Suffix must be a string.")

    # Capitalize only the core text (not the prefix or suffix)
    if capitalize and text:
        text = text[0].upper() + text[1:]

    # Compose the final string (prefix + text + suffix)
    result = f"{prefix}{text}{suffix}"

    # Trim to max_length if applicable
    if max_length is not None:
        result = result[:max_length]

    return result

def get_user_input():
    
    print("Welcome to the Text Formatter!")

    # Get the text
    user_text = input("Enter the text to format: ")

    # Check if the text is alphabetic
    if not isinstance(user_text, str) or not user_text.isalpha():
        raise TypeError("Text must be a string containing only alphabetic characters.")

    # Prefix 
    add_prefix = input("\nDo you want to add a prefix? (yes/no): ").lower()
    if add_prefix not in ["yes", "no"]:
        raise ValueError("Invalid response for prefix. Enter 'yes' or 'no'.")
    prefix = ""
    if add_prefix == "yes":
        prefix = input("Enter the prefix: ")
        # Ensure prefix is a valid string
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string.")

    # Suffix choice 
    add_suffix = input("\nDo you want to add a suffix? (yes/no): ").lower()
    if add_suffix not in ["yes", "no"]:
        raise ValueError("Invalid response for suffix. Enter 'yes' or 'no'.")
    suffix = ""
    if add_suffix == "yes":
        suffix = input("Enter the suffix: ")
        # Ensure suffix is a valid string
        if not isinstance(suffix, str):
            raise TypeError("Suffix must be a string.")

    # Capitalization 
    capitalize_input = input("\nDo you want to capitalize the first letter? (yes/no): ").lower()
    if capitalize_input not in ["yes", "no"]:
        raise ValueError("Invalid response for capitalization. Enter 'yes' or 'no'.")
    capitalize = capitalize_input == "yes"

    # Max length 
    max_length_input = input("\nEnter maximum length (leave blank for no limit): ")
    if max_length_input and not max_length_input.isdigit():
        raise ValueError("Maximum length must be a valid integer.")
    max_length = int(max_length_input) if max_length_input else None

    return user_text, prefix, suffix, capitalize, max_length

if __name__ == "__main__":
    # Get the user input with the options 
    try:
        user_text, prefix, suffix, capitalize, max_length = get_user_input()

        # Call the function so that the user input datas 
        formatted_text = format_text(user_text, prefix, suffix, capitalize, max_length)

        # Printing our result
        print(f"\nFormatted text: {formatted_text}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
