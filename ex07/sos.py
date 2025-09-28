import sys


def main():
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
        return

    message = sys.argv[1].upper()
    # for char in message:
    #     if char not in NESTED_MORSE:
    #         print("AssertionError: the arguments are bad")
    #         return
    if (not all(char in NESTED_MORSE for char in message)):
        print("AssertionError: the arguments are bad")
        return

    # morse_message = ""
    # for char in message:
    #     morse_message += NESTED_MORSE[char]
    morse_message = "".join(NESTED_MORSE[char] for char in message)
    print(morse_message)


if __name__ == "__main__":
    main()
