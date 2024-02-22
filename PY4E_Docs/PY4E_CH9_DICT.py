# PY4E CHAPTER 9 DICTIONARIES
# By Roland Udvari
# Created 1-30-2024

# counts = dict()
# names = ['chev', 'chew', 'zgian', 'chew', 'chev', 'chew']
# for name in names :
#     if name not in counts :
#         counts[name] = 1
#     else :
#         counts[name] = counts[name] + 1
# print(counts)
#print(counts['zgian'])
#
# # counts = dict()
# # names = ['chev', 'chew', 'zgian', 'chew', 'chev', 'chew']
# names.append('Roland')
# for name in names :
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# counts = dict()
# print('Enter a line of text.')
# line = input('..')
# words = line.split()
# print(words)
# print(len(words))
# for word in words :
#     counts[word] = counts.get(word, 0) + 1
# print(counts)

# name = input('Enter a text file:')
# if len(name) < 1:
#    name = "romeo.txt"
# handle = open(name)
#
# counts = dict()
# for lines in handle :
#     words = lines.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1
# # --------SAME AS------= counts[word] + 1 --AND-- += 1
#
# bigword = None
# bigcount = None
# for word, count in counts.items() :
#     if bigword is None or bigcount < count :
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)
# print(counts.items())
# print(counts.keys())
# print(counts.values())