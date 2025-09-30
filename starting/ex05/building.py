import sys


def ft_sum(gen):
    count = 0
    for item in gen:
        count += item
    return count


def getUppers(user_input):
    """
    Count uppercase letters in the user input

    Args:
        user_input (str): The input string

    Returns:
        int: Number of uppercase letters
    """
    # Via generator expression. It passes an object that contains
    # 1 for each uppercase letter and can be iterated.
    return ft_sum(1 for c in user_input if c >= 'A' and c <= 'Z')
    # count = 0
    # for c in user_input:
    #     if c >= 'A' and c <= 'Z':
    #         count += 1
    # return count


def getLowers(user_input):
    """
    Count lowercase letters in the user input

    Args:
        user_input (str): The input string

    Returns:
        int: Number of lowercase letters
    """
    return ft_sum(1 for c in user_input if c >= 'a' and c <= 'z')


def getPunctuations(user_input):
    """
    Count punctuation marks in the user input

    Args:
        user_input (str): The input string

    Returns:
        int: Number of punctuation marks
    """

    return ft_sum(1 for c in user_input if c in '.')


def getSpaces(user_input):
    """
    Count spaces in the user input

    Args:
        user_input (str): The input string

    Returns:
        int: Number of spaces
    """
    return ft_sum(1 for c in user_input if c == ' ')


def getDigits(user_input):
    """
    Count digits in the user input

    Args:
        user_input (str): The input string

    Returns:
        int: Number of digits
    """
    return ft_sum(1 for c in user_input if c >= '0' and c <= '9')


def main():
    """
    The main function
    Args:
        None
    Returns:
        None
    """
    # sys.argv is a list of command line arguments
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if (len(sys.argv) == 1):
        user_input = input("What is the text to count?\n")
    else:
        user_input = sys.argv[1]
    upperNum = getUppers(user_input)
    lowerNum = getLowers(user_input)
    puncNum = getPunctuations(user_input)
    spaceNum = getSpaces(user_input)
    digitNum = getDigits(user_input)
    print("The text contains", len(user_input), "characters:")
    print(f"{upperNum} upper letters")
    print(f"{lowerNum} lower letters")
    print(f"{puncNum} punctuation marks")
    print(f"{spaceNum} spaces")
    print(f"{digitNum} digits")


if __name__ == "__main__":
    main()
