# Coursera - Programming fundamentals
# ====================> Longest Sequence in a list <===================== #
# by Roland Udvari
# 2023-03-6

def maxSeq(list):
    num = None
    curseq = 0
    maxseq = 0
    for x in range(len(list)):
        if num is None or list[x] > num :
            curseq += 1
        else:
            curseq = 1
        if maxseq < curseq:
            maxseq = curseq
        num = list[x]
        pass
    return maxseq

list = [0, 1, 2, 3, 1, 2, 3]
print(maxSeq(list))