# ZAD 4.2

def is_palindrome(str):
    """ 
    Checks if the given string is a palindrome.

    A palindrome is a word, phrase, or number that reads the same forward and backward.
    The check is case-sensitive.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Python")
        False
        >>> is_palindrome("Anna")
        False  # Case-sensitive check
        >>> is_palindrome("Anna".lower())  # Correct version
        True
    """
    reverse_str = str[::-1]
    if str == reverse_str:
        return True
    else:
        return False
