def probability_of_two(a1, a2, a3):
    A = 0
    B = 0
    C = 0
    D = 0
    x = a3
    z = a1
    y = a2
    D1 = 0
    while x > 0:
        x-= 1
        if A > 0 or B > 0 or C > 0 or D > 0:
            D1 = 0
            C1 = 0
            A1 = 0
            B1 = 0
            for i in range(C):
                C1 += y
            for i in range(D):
                C1 += z
                A1 += (y-z)
            for i in range(A):
                C1 += z
                A1 += y-z
            for i in range(B):
                D1 += z
                B1 += y-z
            C = C1
            D = D1
            A = A1
            B = B1
        else:
            B += y - z
            D += z
    return C / (a2**a3)
print(probability_of_two(1,6,5))
# this will find the probability of 2 or more successes if given a z/y chance
# of success on iteration x. (z, y, x). as example, 5 rolls of a die where the
# side 3 is a success has input (1, 6, 5) with 1 being the total possibilites
# per iteration that result in success, 6 being the total possibilities, and
# 5 being the iteration count. running this code outputs the chances of 2 or more
# rolls of side 3. this code is painstakingly slow for numbers of most sizes. 
