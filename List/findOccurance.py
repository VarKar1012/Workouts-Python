def find(l):
    # count19 = list(filter(lambda x: x==19, l))
    # count5 = list(filter(lambda x: x==5, l))
    # if len(count19) == 2 and len(count5) >= 3:
    #     print(True)
    # else:
    #     print(False)

    if l.count(19) == 2 and l.count(5) >= 3:
        print(True)
    else:
        print(False)


l = [19, 19, 15, 5, 3, 5, 5, 2]
# l = [19, 19, 1, 5]
# find exactly 2 occurances of 19 and atleast 3 occurances of 5
find(l)