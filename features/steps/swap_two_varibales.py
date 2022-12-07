
def swap_two_variables(a, b): # a = 2, b = 4
    print(f'a = {a}, b={b}')
    swap = a  # 2
    a = b  # 4
    b = swap  # 2
    print(f'a = {a}, b={b}')


swap_two_variables(2, 4)


# solution 1

# swap = a # 2
# a = b # 4
# b = swap # 2
#
# # solution 2
#
# # a, b = b, a
#
#
# # solution 3
#   a = a + b  # 2 + 4 = 6
#   b = a - b  # 6 - 4 = 2
#   a = a - b  # 6 - 2 + 4
#
# print(f'a = {a}, b = {b}')


# #  0(n)
# # new *
# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif:
#             print(i)


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print (f"is not a leap year")

        else:
            print(f' {year} is a leap year')

    else:
        print(f' {year} is not a leap year')


# 2017 is not leap year
# 1900 is not leap year
# 2012 is a leap year
# 2000 is a leap year
is_leap_year(2017) # not a leap year
is_leap_year(1900) # not a leap year
is_leap_year(2012) # a leap year
is_leap_year(2000) # a leap year




