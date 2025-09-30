import numpy as np
from PIL import Image
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


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
    img = ft_load("landscape.jpg")
    # If the image is empty
    if img.size == 0:
        return
    print("Inverts the color of the image received.")
    # Convert to an image
    Image.fromarray(ft_invert(img)).show()
    Image.fromarray(ft_red(img)).show()
    Image.fromarray(ft_green(img)).show()
    Image.fromarray(ft_blue(img)).show()
    Image.fromarray(ft_grey(img)).show()

if __name__ == "__main__":
    main()
