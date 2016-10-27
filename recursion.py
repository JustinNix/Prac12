"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# 5 % 2 = 2
# then 2 + 2 % 2 = 1 therefore, it will equal 3.
# Then it will go 3 + 1 % 2 = 0 which equals 3.
# once n equals 0 the function returns 0 which is added onto 3?
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    if n < 0:
        return 0
    print(n ** 2)
    return do_something(n - 1)

# There is no base case which allows it to exit the loop. so it will go on until it reaches the limit of recursion?
# TODO: 4. use the debugger to step through and see what's actually happening
#do_something(4)


