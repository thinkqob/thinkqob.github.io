e_list = raw_input("Enter you equation: ").split()

if e_list[1] == '+':
    print "%s" % (float(e_list[0]) + float(e_list[2]))
elif e_list[1] == '-':
    print "%s" % (float(e_list[0]) - float(e_list[2]))
elif e_list[1] == '*':
    print "%s" % (float(e_list[0]) * float(e_list[2]))
elif e_list[1] == '/':
    print "%s" % (float(e_list[0]) / float(e_list[2]))
elif e_list[1] == '%':
    print "%s" % (float(e_list[0]) % float(e_list[2]))
elif e_list[1] == '**':
    print "%s" % (float(e_list[0]) ** float(e_list[2]))
