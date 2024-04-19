def reverse_string(word):
    reverse = ""
    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]
    return reverse
