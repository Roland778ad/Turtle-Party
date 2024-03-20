# Coursera Programming Fundamentals CLASS WORK
# Roland Udvari
# 2024-02-26

# =======> Compatibility and Translating to code <==========
# Print star triangle
n = 5
for i in range(1, n+1):
    print(i*'*')
    pass
# -----------> same as <----------
# print * for each line
def print_n_star(n):
    for i in range (1, n+1):
        print('*', end='')
        pass

# print start triangle
def print_star_triangle(n):
    for i in range(1, n+1):
        print(print_n_star(i))
        pass
print(print_star_triangle(n))

#================> Making a COPY of a list <===================
#
# def myfunc(A):
#     # Create a copy of the list and square all of its entries
#     B = A.copy()
#     for i, b in enumerate(B):
#         B[i] = b**2
#
#     # Sum up the entries of each list and return them
#     return [sum(A), sum(B)]
#
#
# mylist = [1, 2, 3]
# result = myfunc(mylist)
# print(result)

#================> Factorial numbers and print(.format)<============
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         fact = 1
#         for i in range(1, n+1):
#             fact *= i
#             print(f"{i}! = {fact}")
#         return fact
#
# v = 5
# sum = 5
# print(f"{v}! = {factorial(v)}")
# print("{}! = {}".format(v, factorial(v)))
# print(f"{v=}")

# ============> Lists <=======================================
#
# def myFn(lst1, lst2):
#     lst1.append(42)
#     lst2 = lst1
#     lst1 = [4, 5, 6]
#     lst2.append(99)
#     print('lst2 is', lst2)
#     return lst1
#
# def main():
#     a = [1, 2]
#     print('a is', a)
#     b = [33, 34]
#     print('b is', b)
#     c = myFn(a, b)
#     print('a post function is', a)
#     print('b post function is', b)
#     print(c)
#     pass
# main()
# --------> List modification <-----------------
#
# a = [1, 2,]
# b = [3]
# c = []
# lst = [a, b, c, a]
# for x in lst:
#     x.append(42)
#     pass
# print(lst)
# # ---------> extracting numbers from lists within lists <-----------
# newlst = list()
# for sublst in lst:
#     for num in sublst:
#         newlst.append(num)
#         pass
#     pass
# print(newlst)
