# Practice Canvas for individual code blocks
# By Roland Udvari
# Created 1-30-2024

# =====================PRIME CHECKER==========================
def is_it_prime(prm):
    if prm <= 1:
        return False
    if prm == 2:
        return True
    if prm % 2 == 0:
        return 'Even numbers cannot be primes'
    prm1 = (prm-1) // 2
    for i in range(3, prm1, 2):
        if prm % i == 0:
            print('This number is divisible by {}'.format(i))
            return False
    return True

# >>>>>>>>>>>>>> Prime checker checker :) <<<<<<<<<<<<<
# def prime_check(num, expected):
#     if is_it_prime(num) != expected:
#         print('Check complete. FAIL for {}'.format(num))
#         pass
#     else:
#         print('Check complete: PASS')
#     pass
# prime_check(1, False)

print("Prime Checker")
while True :
    prm = input("Enter a whole number: ")
    if len(prm) < 1: break
    prm = int(prm)
    print(is_it_prime(prm))

