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
# for i in range(5):
#     print(i)
#     if i > 2 :
#         print("Bigger than 2")
#     elif i == 2 :
#         print("Equal to 2")
#     else:
#         print("Smaller than 2")
# print()
# print("All done")

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
# count = 0
# sum = 0
# print("Before:", count, sum)
# for num in range(1, 15):
#     count = count + 1
#     sum = sum + num
#     print("#", count, "Sum", sum, "Number", num)
# print("All together there were", count, "numbers.")
# print("The sum of all the numbers is", sum, ".")
# print("The average of all the numbers is", sum / count,".")