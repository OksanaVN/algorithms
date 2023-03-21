def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


str_1 = "abced"
str_2 = "bedac"

result = is_anagram(str_1, str_2)
print(result)
