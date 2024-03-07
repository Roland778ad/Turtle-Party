# Practice Canvas for individual code blocks
# By Roland Udvari
# Created 2024-03-05

# =====================> List sum by pairs <==========================
def lstsum(newlst):
    for numsum in range(len(newlst) - 1):
        if len(newlst) - 1 >= numsum + 1:
            newlst[numsum] = (newlst[numsum] + newlst[numsum + 1])
        else :
            break
    newlst.remove(newlst[-1])
    return newlst
# for numsum in range(len(newlst)-1):
#     sumlist.append(newlst[numsum] + newlst[numsum+1])
#     pass

a = [1, 2,]
b = [3]
c = []
lst = [a, b, c, a]
for x in lst:
    x.append(42)
    pass
print(lst)
# ---------> extracting numbers from lists within lists <-----------
newlst = list()
for sublst in lst:
    for numb in sublst:
        newlst.append(numb)
        pass
    pass
print(newlst)
for numsum in range(len(newlst)-1):
    lstsum(newlst)
    print(newlst)

# ---------> splitting single item in list into single characters <---------------


