# PY4E CHAPTER 7 EXTERNAL FILE OPERATIONS
# By Roland Udvari
# Created 1-30-2024

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
