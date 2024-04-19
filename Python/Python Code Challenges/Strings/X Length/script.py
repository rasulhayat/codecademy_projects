def x_length_words(sentence, x):
    words = sentence.split(" ")
    for word in words:
        if len(word) < x:
            return False
    return True
