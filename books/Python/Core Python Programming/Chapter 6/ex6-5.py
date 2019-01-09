"""
a)
def three_letters():
    letters = raw_input("Enter a words: ")
    for i in xrange(len(letters)):
        if i < 1:
            print letters[0], letters[1]
        elif i == len(letters) - 1:
            print letters[-2], letters[-1]
        else:
            print letters[i - 1], letters[i], letters[i + 1]

three_letters()


b)
def two_words():
    first = (raw_input("Enter the first word: ")).strip()
    second = (raw_input("Enter the second word: ")).strip()

    c = 0

    if len(first) != len(second):
        print "not the same words."
    else:
        for i in xrange(len(first)):
            if first[i] == second[i]:
                c += 1
                if c == len(first):
                    print"the same words."
            else:
                print "not the same words."
                break

two_words()


def same_letter():
    words = raw_input('enter a words:')
    words_lists = []
    while words:
        if words in words_lists:
            print "you already enter that."
        else:
            words_lists.append(words)
        print words_lists
        words = raw_input('enter a words:')

same_letter()
"""

