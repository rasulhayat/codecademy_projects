def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys
