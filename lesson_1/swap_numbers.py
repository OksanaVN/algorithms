#swap 2 numbers

def swap_variables(a:int, b:int):
    print(f"Before swap: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")


# a= a + b version 2
# b = a - b
# a = a - b

#a, b = b, a version 3


test_a = 5
test_b = 10

swap_variables(test_a, test_b)


