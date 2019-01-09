def up_down():
    words = raw_input("Enter a words: ")
    words_list = []
    for i in range(len(words)):
        if words[i] == words[i].lower():
            words_list.append(words[i].upper())
        elif words[i] == words[i].upper():
            words_list.append(words[i].lower())
        else:
            print words_list.append(words[i])

    print "".join(words_list)

up_down()
