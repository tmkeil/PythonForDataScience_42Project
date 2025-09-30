import numpy as np
from PIL import Image
from rotate import ft_rotate


def ft_zoom(family: list, start: int, end: int) -> list:
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
    # Slicing (slice the 1. dim and the 2. dim from start to end)
    sliced = a[start:end, start:end]
    return sliced.tolist()


def ft_load(path: str) -> np.array:
    """
    It loads an image with Pillow and converts it to a numpy array.

    Args:
        1. The path to the image.

    Returns:
        A numpy array of the image pixels.
    """
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            print("Error: Unsupported image format.")
            return np.array([])
        print(f"Image format: {img.format}")
        img = img.convert("RGB")
        a = np.array(img)
        return a
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])


def main():
    img = ft_load("animal.jpeg")
    # If the image is empty
    if img.size == 0:
        return
    # Slice the image to zoom the 1. and 2. dim.
    zoomed = ft_zoom(img.tolist(), 100, 500)
    # Get an array from the sliced list.
    zoomed_array = np.array(zoomed, dtype=np.uint8)
    print("ndim of zoomed_array: ", zoomed_array.ndim)
    red_chan = zoomed_array[:, :, 2]
    # print(f"The shape of image is: {red_chan.shape}")
    print(red_chan)
    # Transpose the image to rotate it
    red_chan = ft_rotate(red_chan, 90)
    # print("New shape after Transpose: ", red_chan.shape)
    print(red_chan)
    # Convert back to an image
    Image.fromarray(red_chan).show()


if __name__ == "__main__":
    main()
