def invert(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value encountered in input dictionary")
        inverted_dict[value] = key
    return inverted_dict