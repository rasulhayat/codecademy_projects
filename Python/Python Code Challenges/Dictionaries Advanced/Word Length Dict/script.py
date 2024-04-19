def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths
