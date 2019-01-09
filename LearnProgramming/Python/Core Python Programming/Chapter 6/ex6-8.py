def num_to_eng():
    num_eng = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
               9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
               30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
               90: 'ninety', 100: 'one hundred', 1000: 'one thousand', 0: 'zero'}
    num = raw_input('Enter your num: ')

    if int(num) in num_eng.keys():
        print num_eng[int(num)]
    else:
        num.split()
        if len(num) == 2:
            s = int(num[-2]) * 10
            print "%s-%s" % (num_eng[s], num_eng[int(num[-1])])
        elif len(num) == 3:
            "".join(num)
            if int(num[-2:]) in num_eng.keys():
                print "%s hundred and %s" % (num_eng[int(num[-3])],
                                             num_eng[int(num[-2:])])
            elif int(num[-2]) == 0 and int(num[-1]) == 0:
                print "%s hundred" % num_eng[int(num[0])]
            else:
                s = int(num[-2]) * 10
                print "%s hundred and %s-%s" % (num_eng[int(num[-3])],
                                                num_eng[s],
                                                num_eng[int(num[-1])])
        elif len(num) == 4:
            "".join(num)
            if int(num[-2:]) in num_eng.keys():
                if int(num[-3]) == 0:
                    print "%s thousand and %s" % (num_eng[int(num[-4])],
                                                  num_eng[int(num[-2:])])
                else:
                    print "%s thousand %s hundred and %s" % (num_eng[int(num[-4])],
                                                             num_eng[int(num[-3])],
                                                             num_eng[int(num[-2:])])
            elif int(num[-2]) == 0 and int(num[-1]) == 0:
                if int(num[-3]) == 0:
                    print "%s thousand" % num_eng[int(num[0])]
                else:
                    print "%s thousand %s hundred" % (num_eng[int(num[-4])],
                                                      num_eng[int(num[-3])])
            else:
                s = int(num[-2]) * 10
                if int(num[-3]) == 0:
                    print "%s thousand and %s-%s" % (num_eng[int(num[-4])],
                                                     num_eng[s],
                                                     num_eng[int(num[-1])])
                else:
                    print "%s thousand %s hundred and %s-%s" % (num_eng[int(num[-4])],
                                                                num_eng[int(num[-3])],
                                                                num_eng[s],
                                                                num_eng[int(num[-1])])

num_to_eng()
