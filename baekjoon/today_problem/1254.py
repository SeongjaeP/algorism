def is_palindrome(s):
    return s == s[::-1]

def min_additions_to_palindrome(s):
    n = len(s)
    for i in range(n):
        if is_palindrome(s[i:]):
            return i
    return n

s = input().strip()
print(len(s) + min_additions_to_palindrome(s))
print(s)

