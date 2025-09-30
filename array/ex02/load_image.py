import numpy as np
from PIL import Image


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
        print("The shape is : ", a.shape)
        return a
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])


# def main():
#     print(ft_load("landscape.jpg"))


# if __name__ == "__main__":
#     main()
