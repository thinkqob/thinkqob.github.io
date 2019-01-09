def no_space():
    words = raw_input("Enter a string: ")
    if words[0] == " ":
        words = words.lstrip()
    if words[-1] == " ":
        words = words.rstrip()
    print words

no_space()
