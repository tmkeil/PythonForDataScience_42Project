import numpy as np


def ft_check_input(matrix: np.array) -> bool:
    """
    Check if the input is a valid image array and return a tuple of its color channels.

    Args:
        matrix of the image

    Returns:
        bool: True if the input is valid
        tuple: The color channels if the input is valid. Otherwise, False.
    """
    if not isinstance(matrix, np.ndarray):
        print("Error: Input must be a numpy array.")
        return False
    # An image should be a 3D array with 3 channels.
    # The first dim is the height, the second dim is the width,
    # and the third dim is the color channels.
    if matrix.ndim != 3 or matrix.shape[2] != 3:
        print("Error: Input array of wrong shape.")
        return False, None
    return True, (matrix[:, :, 0], matrix[:, :, 1], matrix[:, :, 2])


def ft_invert(matrix: np.array) -> np.array:
    """
    Invert the colors of an image represented as a numpy array.

    Args:
        1. matrix (np.array): A numpy array representing the image.
    Returns:
        A numpy array with inverted colors.
    """
    if ft_check_input(matrix) is False:
        return matrix


def ft_red(matrix: np.array) -> np.array:
    """
    Isolate the red channel of an image represented as a numpy array.

    Args:
        1. matrix (np.array): A numpy array representing the image.
    Returns:
        A numpy array with only the red channel.
    """
    if ft_check_input(matrix) is False:
        return matrix


def ft_green(matrix: np.array) -> np.array:
    """
    Isolate the green channel of an image represented as a numpy array.

    Args:
        1. matrix (np.array): A numpy array representing the image.
    Returns:
        A numpy array with only the green channel.
    """
    if ft_check_input(matrix) is False:
        return matrix


def ft_blue(matrix: np.array) -> np.array:
    """
    Isolate the blue channel of an image represented as a numpy array.

    Args:
        1. matrix (np.array): A numpy array representing the image.
    Returns:
        A numpy array with only the blue channel.
    """
    if ft_check_input(matrix) is False:
        return matrix


def ft_grey(matrix: np.array) -> np.array:
    """
    Convert an image represented as a numpy array to grayscale.

    Args:
        1. matrix (np.array): A numpy array representing the image.
    Returns:
        A numpy array in grayscale.
    """
    check = ft_check_input(matrix)
    if check[0] is False:
        return matrix
    r, g, b = check[1]
    gray = (r + g + b) / 3
