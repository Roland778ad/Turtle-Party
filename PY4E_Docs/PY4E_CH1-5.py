# Python for Everyone Project
# by Roland Udvari
# 1-30-2024

# ===========PRINT ====================================
# For those with a literal sense for the instructions.
# print("one line other than 'hello world'")
# print("\U0001F44D")

# ======================IF, ELIF, ELSE===================
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

# ======================TRY, EXCEPT=====================
# temp = input("what is the current temperature in Fahrenheit? ")
# try :
#     fahr = float(temp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except :
#     print("Use # digits only")

# =================BREAK, CONTINUE================
# while True :
#     line = input(">")
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# ======================LARGEST====================
# largest_so_far = "A"
# print("before", largest_so_far)
# for the_num in ("Hello-world"):
#     if largest_so_far < the_num:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print("The highest value object is", largest_so_far)

# ===============COUNT, SUM, AVERAGE==================
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