#[1,2,3,4,5,,6,7] [3,7,2,1,4,6]
import collections


def find_missing_number(l1, l2):
    arr_dict = collections.defaultdict(int)

    for num in l2:
        arr_dict[num] += 1

    for num in l1:
        if arr_dict[num] == 0:
            return num
        else:
            arr_dict[num] += 1


    # l1.sort()
    # l2.sort()

    # for i in range(len(l2) -1):
    #     if l1[i] != l2[i]:
    #         return l1[i]
    #
    # return l1[-1]

    # for num1, num2 in zip(l1, l2):
    #     if num1 != num2:
    #         return num1



test_l1 = [1,2,3,4,5,6,7]
test_l2 = [3,7,2,1,4,6]
result = find_missing_number(test_l1, test_l2)
print(result)


