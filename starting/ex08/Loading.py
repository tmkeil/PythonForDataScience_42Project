def ft_tqdm(lst: range) -> None:
    """
    Custom impl. of tqdm. Because it is a func with yield,
    it returns a generator when called once.
    The generator can be iterated over in a for-loop
    (next() is called at each loop).
    At each loop, the function runs until the next yield statement,
    where it returns the value and pauses the function's
    state until the next next() call.

    Args:
        lst: The range to iterate over

    Returns:
        Generator yielding each value
    """
    total = len(lst)
    for i, val in enumerate(lst, 1):
        # i goes from 1 to total. val goes from lst[0] to lst[-1]
        percent = int((i / total) * 100)
        bar_len = 170
        filled = int(bar_len * i / total)
        # | ========>                  |
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        print(f"\r{percent}%|{bar}| {i}/{total}", end="")
        # yield makes sure, a value is returned.
        # "for elem in ft_tqdm(range(333))"
        # needs it as a generator to iterate over in each loop
        # yields advantage is, it saves memory as it doesn't store
        # all values (for example in a list, that would be 333 values) at once
        # The specific value doesn't matter here. The loop just needs a
        # generator to yield a value at each step. In the first loop,
        # it stops before yield val, in the second loop it stops before
        # yield val again, and so on. At the last yield, the generator
        # is finished and the loop ends.
        yield val


# def main():
#     """
#     The main function

#     Args:
#         None

#     Returns:
#         None
#     """


# def tester():
#     from time import sleep
#     from tqdm import tqdm
#     from Loading import ft_tqdm
#     # ft_tqdm returns a generator. The for-loop calls next(),
#     # which runs the function up to the next yield.
#     # At each yield, it returns the value and pauses the function's state.
#     for elem in ft_tqdm(range(333)):
#         sleep(0.005)
#     print()
#     for elem in tqdm(range(333)):
#         sleep(0.005)
#     print()


# if __name__ == "__main__":
#     # tester()
#     main()
