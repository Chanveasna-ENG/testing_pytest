def find_missing_letter(chars):
    for index, i in enumerate(chars):
        if ord(i) + 1 != ord(chars[index+1]):
            return chr(ord(i)+1)
