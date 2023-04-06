# 1
#
# def below_arith_mean(arr):
#     arith_mean = sum(arr) / len(arr)
#     final_list = []
#     for element in arr:
#         if element < arith_mean:
#            final_list.append(element)
#     return  final_list
#
#
# test_list = [1, 3, 5, 6, 4, 10, 2, 3]
# test_result = below_arith_mean(test_list)
# print(test_result)
#


# 2

def find_2_lowest(arr):
    arr.sort()
    return arr[:2]


test_list = [198, 3, 4, 9, 10, 9, 2]
test_result = find_2_lowest(test_list)
print(test_result)