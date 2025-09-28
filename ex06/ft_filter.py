def ft_filter(function, iterable):
    """
    Custom impl. of filter

    Args:
        1. The function to apply to each element of the iterable
        2. The iterable to filter

    Returns:
        A generator with the filtered elements
    """
    return ([item for item in iterable if function is None or function(item)])
