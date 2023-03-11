#Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.



def sum_of_digits(n: int):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i

        print(f"Sum of {n} is {total_sum}")


n = 5

sum_of_digits(5)


#Find the max number from 3 values.
#Example: 124, 21, 32. Result = 124.

def find_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    print(max_num)


find_max(124, 21, 32)


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def count_odd_even(n):  # USED CHAT GPT for this one, I tried myelf very similar but it didn't work, and I don't hhave enougth knowledge to figure it out
    odd_count = 0
    even_count = 0
    for i in str(n):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(odd_count, even_count)

count_odd_even(34560)


