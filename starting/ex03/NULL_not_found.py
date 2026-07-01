def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    # object != object means NaN != NaN is True because NaN is not equal to anything
    elif type(object) == float and object != object:
        print(f"Cheese: nan {type(object)}")
        return 0
    elif type(object) == bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif type(object) == int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) == str and object == '':
        print(f"Empty: {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1

# if __name__ == "__main__":
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ''
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))
