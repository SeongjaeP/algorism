import re

def is_valid_string(s):
    pattern = re.compile(r'^(pi|ka|chu)*$')
    if pattern.match(s):
        return "YES"
    else:
        return "NO"


s = input().strip()

print(is_valid_string(s))


