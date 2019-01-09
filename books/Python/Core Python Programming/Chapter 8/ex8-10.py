def count_words(line):
    aeiou = 'aeiou'
    aeioucounts = 0
    for s in line:
        if s.isalpha():
            if s in aeiou:
                aeioucounts += 1
    print aeioucounts

    words = len([word for word in line.split()])
    print "%s words"  % words

print count_words("a dog is barking")
