
def remove_item_from_list(my_list, n):
    for i in range(len(my_list) - 1):
        if my_list[i] == n:
            my_list.pop(i)
    print(my_list)


my_list = [1, 6, 24, 7, 2, 10, 2, 22, 2, 2, 2, 2]
my_second_list = [9, 15]

print(my_list)
remove_item_from_list(my_list, 7)

# print(my_list + my_second_list)
# print(my_list)
#
# my_list.append(77)
# total_ones = my_list.count(1)
# total_twos = my_list.count(2
#                            )
# # my_list.clear()
#
# # print(my_list)
#
# print(total_ones)
# # print(total_twos)
#
# print(my_list.index(24))

# my_list.insert(1, 99) # add
# index_to_pop = my_list.index(24)
# my_list.pop(index_to_pop)
# # my_list.pop(3) # remove by index
# print(my_list)

# my_list.remove(2)
# print(my_list)

# my_list.reverse()
#
# my_list.sort()
#
# print(my_list)
#

