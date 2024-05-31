# Coursera - Programming fundamentals
# ====================> Longest Sequence in a list <===================== #
# by Roland Udvari
# 2023-03-6

def maxSeq(data):
    num = None
    curseq = 0
    maxseq = 0
    for x in range(len(data)):
        if num is None or data[x] > num :
            curseq += 1
        else:
            curseq = 1
        if maxseq < curseq:
            maxseq = curseq
        num = data[x]
        pass
    return maxseq

data = [-1, 2, 5, 7, 1, 2, 3]
print(maxSeq(data))