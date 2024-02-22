# PY4E CHAPTER 8 LISTS
# By Roland Udvari
# Created 1-30-2024

friends = ["Joe", "Glenn", "Sally"]
print(friends)
print(len(friends))
print(friends[1])
print()

for friend in friends :
    print("Happy New Year,", friend + "!")

for x in range(len(friends)-1) :
    print('Happy Birthday,', friends[1] + '!')


listnum = [1, 56, 98, 0, 33, 687, 1598]
print('Numbers so far:', listnum)
while True :
    inp = input('Add any numbers to this list (when finished, type "done"): ')
    if inp == 'done' :
        break
    splitinp = inp.split(',')
    for numb in splitinp :
        listnum.append(int(numb))
print(listnum)
listnum.sort()
print('All numbers in order:', listnum)
print('The lowest number on your list is', min(listnum))
print('The highest number on your list is', max(listnum))
print('You have entered', len(listnum), 'number(s).')
sumnum = str(sum(listnum))
print('The sum of all numbers is', sumnum + '.')
print('The average of all numbers is:', sum(listnum) / len (listnum))
print('DONE')
