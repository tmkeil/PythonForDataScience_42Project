import sys
from ft_filter import ft_filter


def ft_isinstance(var, type_):
    """
    Custom impl. of isinstance

    Args:
        var: The variable
        type_: The type to check against

    Returns:
        A tuple (isType true/false, value of the variable)
    """
    # Check if the argument is a valid integer
    if type_ == int:
        try:
            value = int(var)
            return (True, value)
        except ValueError:
            return (False, None)
    # Check if the argument is a valid string
    elif type_ == str:
        try:
            value = str(var)
            return (True, value)
        except ValueError:
            return (False, None)
    else:
        return (False, None)


def main():
    """
    The main function

    Args:
        None

    Returns:
        None
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    isstr, strVal = ft_isinstance(sys.argv[1], str)
    if (isstr is False or strVal == ""):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    isnum, numVal = ft_isinstance(sys.argv[2], int)
    if (isnum is False or numVal < 0):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    words = strVal.split(" ")
    # Print the words in strVal, that are longer than numVal
    # A word is separated by a space
    # Lambda function is used to pass the first arg as a function.
    # x: Each word in the list
    print([word for word in ft_filter(lambda x: len(x) > numVal, words)])


if __name__ == "__main__":
    main()
