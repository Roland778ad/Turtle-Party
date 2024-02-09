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


# listnum = [1, 56, 98, 0, 33, 687, 1598]
# print('Numbers so far:', listnum)
# while True :
#     inp = input('Add any numbers to this list (when finished, type "done"): ')
#     if inp == 'done' :
#         break
#     splitinp = inp.split(',')
#     for numb in splitinp :
#         listnum.append(int(numb))
# print(listnum)
# listnum.sort()
# print('All numbers in order:', listnum)
# print('The lowest number on your list is', min(listnum))
# print('The highest number on your list is', max(listnum))
# print('You have entered', len(listnum), 'number(s).')
# sumnum = str(sum(listnum))
# print('The sum of all numbers is', sumnum + '.')
# print('The average of all numbers is:', sum(listnum) / len (listnum))
# print('DONE')

#CHAPTER 9 DICTIONARIES
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
# handle = open(name)
#
# counts = dict()
# for lines in handle :
#     words = lines.split()
#     for word in words :
#         counts[word] = counts.get(word, 0) + 1
#
# bigword = None
# bigcount = None
# for word, count in counts.items() :
#     if bigword is None or bigcount < count :
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)

# CHAPTER 10 TUPLES
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

# CHAPTER 11 REGULAR EXPRESSIONS
hand = open('sample_text.txt')
# for lines in hand :
#     if '@' in lines :
#         words = lines.split()
#         for email in words :
#             if '@' in email :
#                 print(email)

# print ()
# import re
#
# print()
# hand = open('sample_text.txt')
#
# # for line in hand :
# #     line = line.rstrip()
# #     if re.search('^From:', line) :
# #         print(line)
#
# # for lines in hand :
# #     if lines.startswith("From") :
# #         line = lines.rstrip()
# #         print(re.findall('^From (\S+@\S+)', line))
# emails = list()
# for lines in hand :
#     line = lines.strip()
#     y = re.findall('^From (.*@[^ ]*)', line)
#
#     if len(y) != 1 :continue
#     emails.append(y)
# print(len(emails))
# print(emails)

# CHAPTER 10 NETWORK

#==============SOCKET LIBRARY===============
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()

#==============URLIB LIBRARY==============

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# header = fhand.getheaders()
# print(header)
# for line in fhand :
#     print(line.decode().strip())

#==========BEAUTIFULSOUP==============

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import re
# url = input('Enter web address: ')
# html = urllib.request.urlopen(url).read().decode()
#
#soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
#
# words = html.split()
# #print(words)
# for href in words:
#     if href.startswith('href'):
#        print(href[6:(-1)])
#        hrefcln = re.findall('"(\\S*)"', href)
#        print(hrefcln)

