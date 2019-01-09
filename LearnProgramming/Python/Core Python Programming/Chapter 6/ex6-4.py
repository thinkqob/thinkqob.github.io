def average():
    list_org = raw_input("Enter some score: ").split()
    print list_org
    r = 0
    for i in range(len(list_org)):
        r += float(list_org[i])
    print r / len(list_org)

average()
