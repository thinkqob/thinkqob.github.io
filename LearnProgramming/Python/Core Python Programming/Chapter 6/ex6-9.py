def min_to_hour():
    time = int(raw_input("Enter minutes: "))
    hour = time // 60
    mins = time % 60
    if mins == 0:
        print "%s hours" % hour
    elif hour == 0:
        print "%s minutes" % mins
    else:
        print "%s hours %s minutes" % (hour, mins)

min_to_hour()
