# Coursera Programming Fundamentals
# Retirement Calculator Project
# Roland Udvari
# 2024-02-29

# def retirement(length, inv, intr, cont):
#     intr = intr/12/100
#     for i in range(length):
#         inv += inv * intr + cont
#         print('Your balance at end of month', i, 'is:', inv)
#         pass
#     return inv

# wlength = int(input('How long is employment (in months)?: '))
# winv = float(input('What is the initial investment?: '))
# wintr = float(input('What will be the annual interest rate during employment?: '))
# wcont = float(input('What will be your monthly contribution?: '))
# rlength = int(input('How long is retirement (in months)?: '))
# rintr = float(input('What will be the annual interest rate during retirement?: '))
# rcont = (float(input('What will be the monthly withdrawal during retirement?: ')))*-1
#
#
# wlength = int(3)
# winv = float(10000)
# wintr = float(12)
# wcont = float(1000)
# rlength = int(2)
# rintr = float(1.2)
# rcont = float(2000)*-1
#
# rinv = retirement(wlength, winv, wintr, wcont)
# print('Balance at time of retirement will be', rinv)
# rend = retirement(rlength, rinv, rintr, rcont)

# ==========================> Class Test Submission <=================================
#  calculate retirement savings
#  start_age is the age (in months) when we start the calculation
#  initial is the initially saved balance at the start
#  working is a three tuple (months, contribution, rate of return)
#  retired is a three tuple (months, contribution, rate of return)
def calculateRetirement1(start_age, initial, working, retired):
    for i in range(working[0]):
        print('Age {0:3d} month {1:2d} you have ${2:.2f}'.format(int(start_age / 12), int(start_age % 12), initial))
        initial += working[1] + (initial * working[2])
        start_age += 1

    for i in range(retired[0]):
        print('Age {0:3d} month {1:2d} you have ${2:.2f}'.format(int(start_age / 12), int(start_age % 12), initial))
        initial += retired[1] + (initial * retired[2])
        start_age += 1
    pass
# ---------- > Same as <-------------------------------------------------
def calculateRetirement(start_age, initial, working, retired):
    work_b_c = balance_calc(start_age, initial, working)
    balance_calc(work_b_c[0], work_b_c[1], retired)
    pass

def balance_calc(age, balance, status):
    for i in range(status[0]):
        print('Age {0:3d} month {1:2d} you have ${2:.2f}'.format(int(age / 12), int(age % 12), balance))
        balance += status[1] + (balance * status[2])
        age += 1
    return age, balance
# ----------------------------------------------------------------------

def main():
    working=(489,1000,0.045/12)
    retired=(384,-4000, 0.01/12)
    calculateRetirement(327, 21345, working, retired)
    pass

if __name__=="__main__":
    main()
    pass