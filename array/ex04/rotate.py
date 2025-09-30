import numpy as np


def ft_rotate(matrix: np.array, angle: int) -> np.array:
    """
    Rotate an array

    Args:
        1. matrix (np.array)
        2. angle

    Returns:
        Rotated np.array
    """
    if angle not in [0, 90, 180, 270]:
        print("Error: Angle must be 90, 180, or 270 degrees.")
        return matrix
    if not isinstance(matrix, np.ndarray):
        print("Error: Input must be a numpy array.")
        return matrix
    if angle == 0:
        return matrix
    elif angle == 90:
        return np.rot90(matrix, k=-1)
    elif angle == 180:
        return np.rot90(matrix, k=2)
    elif angle == 270:
        return np.rot90(matrix, k=1)
