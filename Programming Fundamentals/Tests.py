# Coursera Programming Fundamentals
# Roland Udvari
# 2024-02-28

# n = 6
# lst = list()
# for i in range(0, n*3):
#     x = n * (-n) + (i * i)
#     lst.append(x)
# print(lst)
# # --------------------- Same as -----------------------
# lst1 = list()
# x = -n * n
# for i in range(1, n*3+1):
#     lst1.append(x)
#     x = x + (i * 2) -1
# print(lst1)
# ===================> week 2 test <=========================
def anotherFunction(a, b):
    answer = 42
    x = 0
    print('In anotherFunction({}, {})'.format(a, b))
    while b > a:
        print('a = {}, b = {}'.format(a, b))
        answer = answer + (b - a)
        # !these DO NOT get updated in the HEAP, only refer to THIS function!
        b -= x
        a += x // 2
        x += 1
        pass
    return answer

def someFunction(x, y):
    a = x + y
    if x < y:
        for i in range(x):
            print('In the loop with i = {}, a = {}'.format(i, a))
            a = a + x
            pass
        pass
    else:
        y = anotherFunction(y, a + 4)
        pass
    return a * y

def main():
    x = 2
    a = someFunction(x, 3)
    print('a = ' + str(a))
    print('x = ' + str(x))
    b = someFunction(3, x)
    print('b = ' + str(b))
    print('x = ' + str(x))
    return 0

main()
# =================> Retirement Calculator in seperate file <=============================
