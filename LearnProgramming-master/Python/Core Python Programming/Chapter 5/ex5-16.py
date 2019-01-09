def pay():
    total = float(raw_input("Enter opening balance: "))
    month = float(raw_input("Enter monthly payment: "))
    print "    \tAmount\tRemaining"
    print "Pymt#\t Paid\t Balance"
    print "-----\t------\t---------"
    print "  0\t    $ 0.00\t $%.2f" % total

    num = 1
    while num < 8:
        if (total - month) > 0:
            total -= month
        else:
            month = total
            total = 0
        print "%3d\t    $%5.2f\t $%6.2f" % (num, month, total)
        num += 1

print pay()
