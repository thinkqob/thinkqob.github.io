score = int(raw_input("Enter your score: "))

if 90 <= score <= 100:
    print "You got an A."
elif 80 <= score <= 89:
    print "You got an B."
elif 70 <= score <= 79:
    print "You got an C."
elif 60 <= score <= 69:
    print "You got an D."
elif 0 <= score <= 60:
    print "You got an F."
else:
    print "You got nothing."
