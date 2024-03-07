# Coursera Programming Fundamentals
# Retirement Calculator Project
# Roland Udvari
# 2024-02-29

def retirement(length, inv, intr, cont):
    intr = intr/12/100
    for i in range(length):
        inv += inv * intr + cont
        print('Your balance at end of month', i, 'is:', inv)
        pass
    return inv

# wlength = int(input('How long is employment (in months)?: '))
# winv = float(input('What is the initial investment?: '))
# wintr = float(input('What will be the annual interest rate during employment?: '))
# wcont = float(input('What will be your monthly contribution?: '))
# rlength = int(input('How long is retirement (in months)?: '))
# rintr = float(input('What will be the annual interest rate during retirement?: '))
# rcont = (float(input('What will be the monthly withdrawal during retirement?: ')))*-1


wlength = int(3)
winv = float(10000)
wintr = float(12)
wcont = float(1000)
rlength = int(2)
rintr = float(1.2)
rcont = float(2000)*-1

rinv = retirement(wlength, winv, wintr, wcont)
print('Balance at time of retirement will be', rinv)
rend = retirement(rlength, rinv, rintr, rcont)
