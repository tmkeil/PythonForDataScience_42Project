import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    It slices a 2D array (list of lists).

    Args:
        1. A list of lists.
        2. Start index.
        3. End index.

    Returns:
        A sliced list.
    """
    # Check if family is a list of lists
    if not isinstance(family, list) or \
       not all(isinstance(sub, list) for sub in family):
        print("Error: List must be a list of lists")
        return []
    # Check if every list has the same length
    if not all(len(sub) == len(family[0]) for sub in family):
        print("Error: All rows must have the same length.")
        return []
    # Check if the start/end are int
    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: Start and end must be integers.")
        return []

    # Convert to np array to apply slicing
    a = np.array(family)
    print("My shape is : ", a.shape)

    # Slicing
    sliced = a[start:end]
    print("My new shape is : ", sliced.shape)
    return sliced.tolist()


# def main():
#     family = [[1.80, 78.4],
#             [2.15, 102.7],
#             [2.10, 98.5],
#             [1.88, 75.2]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))


# if __name__ == "__main__":
#     main()
