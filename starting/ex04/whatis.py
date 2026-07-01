import sys


def isnum(s):
    """
    Check if a string is an integer

    Args:
        s (str): The string to check

    Returns:
        tuple: (bool, int)
    """
    try:
        n = int(s)
        return True, n
    except ValueError:
        return False, -1


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
    if len(sys.argv) == 1:
        return
    is_num, num = isnum(sys.argv[1])
    if not is_num:
        print("AssertionError: argument is not an integer")
        return

    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
