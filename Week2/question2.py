def charCount(t):
    """
    Reads a text file and computes the frequency of each unique character excluding whitespaces.

    Args:
        t (str): The path to the text file.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_dict = {}
    with open(t, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if not char.isspace():  # Exclude whitespaces
                    char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict



