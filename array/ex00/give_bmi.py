import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    It calculates BMI with height and weight lists.

    Args:
        1. List of heights in m.
        2. List of weights in kg.

    Returns:
        List of BMIs.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: Height and weight must be lists.")
        return []
    if len(height) != len(weight):
        print("Error: Height and weight lists must have the same length.")
        return []
    if not all(isinstance(h, (int, float)) and h > 0 for h in height):
        print("Error: Heights must be positive numbers.")
        return []
    if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
        print("Error: Weights must be positive numbers.")
        return []

    # We convert the lists to np arrays because we can not do element-wise
    # operations on lists. np arrays support element-wise operations.
    height_m = np.array(height)
    weight_kg = np.array(weight)
    # bmi = weight (kg) / (height (m) * height (m))
    bmi = weight_kg / (height_m ** 2)
    # return [val for val in bmi]
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI values and return a list of booleans

    Args:
        1. List of BMI values.
        2. The limit.

    Returns:
        List of booleans.
    """
    bmi_array = np.array(bmi)
    return (bmi_array > limit).tolist()


# def main():
#     height = [2.71, 1.15, 2]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()
