def compute_sum(n):
    sum = 0
    for i in range(1, n + 1):   # range(1, 6) -------- 1,2,3,4, 5
        sum = sum + i
    return sum


# def compute_sum_1(n):
#     sum = (n * (n+1))/2
#     return int(sum)
#

#########################################################################################################################


# def max_value(a,b, c):
#     if a > b:
#         if a > c:
#             print(f"{a} is the greatest")
#         else:
#             print(f"{c} is the greatest")
#     elif b > c:
#         print(f"{b} is the greatest")
#     else:
#         print(f"{c} is the greatest")


########################################################################################
# Iteration 1: Value of i  = 1, sum = 0 + 1 = 1
# Iteration 2: Value of i  = 2, sum =1 + 2 = 3
# Iteration 3: Value of i  = 3, sum =3 + 3 = 6
# Iteration 4: Value of i  = 4, sum =6 + 4 = 10
# Iteration 5: Value of i  = 5, sum =10 + 5 = 15


#
# print(max_value(9, 10, 1))


def count(n):
    odd_count  = 0
    even_count = 0
    while(n > 0):
        cat = n % 10
        if cat %2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        n = int(n/10)
    print(f"Even Count: {str(even_count)}")
    print (f"Odd Count {str(odd_count)}")



count(34560)
