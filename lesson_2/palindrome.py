def is_palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False


test_s_positive = "radar"
test_s_negative = "radax"
result_positive = is_palindrome(test_s_positive)
print(result_positive)

result_negative = is_palindrome(test_s_negative)
print(result_negative)