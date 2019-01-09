def hour_to_min():
    time = raw_input("What's the time? :").split(':')
    print "%s minutes" % (int(time[0]) * 60 + int(time[1]))

hour_to_min()
