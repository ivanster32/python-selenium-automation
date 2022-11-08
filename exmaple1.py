# def sum_and_mult(arr):
#     sum_result = 0
#     mult_result = 1
#     for i in arr:
#         sum_result += sum_result + i
#         sum_result *= i
#
#
#     return [sum_result, mult_result]
#
#
# test_list = [1,7 ,3] # [11, 21]
#
# result_list = sum_and_mult(test_list)
# print(test_list)
# print("sum " + str(result_list[0]))
# print("multiplication: ")


#
# def sum_between_min_and_max(arr):
#     min_item = max_item = arr[0]
#     min_index = max_index = i = 0
#
#     while i < len(arr):
#         if arr [i] > max_item:
#             max_item = arr[i]
#             max_index = i
#         if arr[i] < min_item:
#             min_item = arr[i]
#             min_index = i
#         i += 1
#
#    return sum(arr[min(min )



def buy_and_sell_stock(prices):
    max_sum = 0
    curr_sum + 0

    for i in range(len(prices))::
    curr_sum = curr_sum + prices[ i + 1] - prices[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0

    return max_sum

prices = [7 , 1 5 , 3, 6, 4] # return: 5
result = buy_and_sell_stock(prices)
print(result)



