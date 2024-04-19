def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other
