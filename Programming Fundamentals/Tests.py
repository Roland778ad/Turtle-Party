# Coursera Programming Fundamentals
# Roland Udvari
# 2024-02-28

# n = 6
# lst = list()
# for i in range(0, n*3):
#     x = n * (-n) + (i * i)
#     lst.append(x)
# print(lst)
# # --------------------- Same as -----------------------
# lst1 = list()
# x = -n * n
# for i in range(1, n*3+1):
#     lst1.append(x)
#     x = x + (i * 2) -1
# print(lst1)
# =================> Retirement Calculator in seperate file <=============================
# =================> Max(list) <=========================
def listMax(list):
    max = None
    if list == None or len(list) < 0:
        return 'None'
    for i in list:
        if max == None or i > max:
            max = i
            pass
        pass
    return max

def doTest(list):
    print('listMax(',end='')
    if list == None:
        print('None) is ',end='')
        pass
    else:
        n = len(list)
        print('[',end='')
        for i in range(0, n):
            print('{}'.format(list[i]),end='')
            if i < n - 1:
                print(', ',end='')
                pass
            pass
        print(']) is ',end='')
        pass
    max = listMax(list)
    if max == None:
        print('None')
        pass
    else:
        print('{}'.format(max))
        pass
    pass

def main():
    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    doTest(list1)
    doTest(list2)
    doTest(list3)
    doTest(None)
    doTest([])
    return 0

if __name__ == '__main__':
    main()
    pass
