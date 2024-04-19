def count_multi_char_x(word, x):
    splits = word.split(x)
    return len(splits) - 1
