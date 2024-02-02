# Practice Canvas for individual code blocks
# By Roland Udvari
# Created 1-30-2024

# PRIME CHECKER
# print("Let's see if I can figure out if a number is a prime number")
# prm = input("What's your number: ")
# prm1 = int(prm)/2
#
# for i in range(2, prm1):
#     if int(prm) % i == 0:
#         print("This is not a prime number.")
#     if int(prm) % i > 0:
#         print("This is a prime number.")

# IF, ELIF, ELSE
# while True :
#     word = input('word: ')
#     if word > 'banana' :
#         print(word,"comes after banana")
#     elif word < 'banana' :
#         print(word, "comes before banana")
#     else :
#         print("Your word is bananas...")
#         break
# print('Done')

# TRY, EXCEPT
# temp = input("what is the current temperature in Fahrenheit? ")
# try :
#     fahr = float(temp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except :
#     print("Use # digits only")

# BREAK, CONTINUE
# while True :
#     line = input(">")
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# LARGEST
# largest_so_far = "A"
# print("before", largest_so_far)
# for the_num in ("Hello-world"):
#     if largest_so_far < the_num:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print("The highest value object is", largest_so_far)

# COUNT, SUM, AVERAGE
# print("To sum it all up...")
# input1 = int(input("Give me a number"))
# count = 0
# sum = 0
# #print("Before:", count, sum)
# for num in range(input1+1):
#     count = count + 1
#     sum = sum + num
#     #print("#", count, "Sum", sum, "Number", num)
# avg = str(sum / count)
# sum = str(sum)
# print("All together there were", count, "numbers.")
# print("The sum of all the numbers is", sum + ".")
# print("The average of all the numbers is", avg + ".")

# ch6 SLICE STRIP STRINGS
# src = 'X-DSPAM-confidence: 0.0475 '
# i = src.find(':')
# print('position of :', i)
# a = src[i+1:]
# print('string slice of the source data', a)
# b = a.strip()
# print('stripped string', b)
# c = float(b)
# print("number with float test", c+42)
# print()
# piece = float(src[src.find(':')+1:].strip())
# print('single line code with float test: ', piece+42)

# ch7 EXTERNAL FILE OPERATIONS
# while True :
#     file = input('Enter file, ot type '"Quit"' to quit: ')
#     if file != "Quit" :
#         try :
#             data = open(file)
#             break
#         except :
#             print("Invalid file.")
#             continue
#     print('Done')
#     quit()
#
# count = 0
# for line in data:
#     count = count+1
# print('Line count of file:', count)
#
# data = open(file)
# inp = data.read()
# print("There are ", len(inp), 'characters in this file.')
# print(inp[:21])
#
# data = open(file)
# count = 0
# for fromline in data :
#     fromline = fromline.rstrip()
#     if not fromline.startswith("From") :
#         continue
#     if not 'uct.ac.za' in fromline :
#         continue
#     count = count + 1
#     print(count, fromline)
# print('done')

# CH8 LISTS
# friends = ["Joe", "Glenn", "Sally"]
# print(friends)
# print(len(friends))
# print(friends[1])
# print()
#
# for friend in friends :
#     print("Happy New Year,", friend + "!")
#
# for x in range(len(friends)-1) :
#     print('Happy Birthday,', friends[1] + '!')


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


