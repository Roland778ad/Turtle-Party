# PY4E CHAPTER 10 TUPLES
# By Roland Udvari
# Created 1-30-2024

# (k, v) = (4, 7)
# print(k)
# dictionary = {'c':99}
# dictionary['a'] = 2
# dictionary['b'] = 67
# print(dictionary)
# print(dictionary['a'])
# ((x, y, z)) = dictionary.items()
# tuple = (x,y,z)
# print(tuple[1])
# print()
#
# lst = list()
# for k, i in dictionary.items() :
#     print(k, i)
#     lstitem = (i, k)
#     lst.append(lstitem)
# lst = sorted(lst, reverse=True)
# print(lst)
# print()
#
# print(sorted ( [ ( i, k) for k, i in dictionary.items()], reverse=True))

#-----TURN DICTIONARY TO TUPLE TO LIST------
# stuff = {'candy': 3, 'cand' : -1, 'can' : 9}
# x, y, z = stuff.items()
# a = [x[1], y[1], z[1]]
# a.sort(reverse=True)
# print(a)
#------------All different data types-------------
# dict = {56.0 : 2}
# byt = b'abc'
# set = {56, 78}
# list = ['edge', 23]
# tup = ('tuples', 53, 'g14')
# int = 864
# flt = 12.6
# dtatyp = [dict, byt, set, list, tup, int, flt]
# for typ in dtatyp:
#     try:
#         if len(typ) == 1:
#             print(typ, 'is a', type(typ), 'type data.')
#         else :
#             print(typ, 'is a', type(typ), 'type data set.')
#     except:
#         print(typ, 'is a', type(typ), 'type data.')