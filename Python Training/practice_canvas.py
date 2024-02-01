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

# SLICING STRINGS
word = 'bananaxblimeynana'
i = word.find('x')
i2 = word.find("na", i+1)
print('x is in',i, 'position')
print('the next ''na'' after ''x'' is in', i2, 'position')
print('the text between ''x'' and ''na'' is:', word[i+1:i2])
