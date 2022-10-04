import sys
from string import ascii_lowercase, ascii_uppercase

list_upper = list(ascii_uppercase)
list_lower = list(ascii_lowercase)

n = sys.stdin.readline().rstrip()

for i in n:
    idx = 0
    if i in list_lower:
        idx = list_lower.index(i)
        idx += 13
        if idx >= len(list_lower):
            idx -= 26
        print(list_lower[idx], end='')
    elif i in list_upper:
        idx = list_upper.index(i)
        idx += 13
        if idx >= len(list_upper):
            idx -= 26
        print(list_upper[idx], end='')
    else:
        print(i, end='')

#  if 'a'<=x and x<='z':
#         x=ord(x)+13
#         if x>122:
#             x-=26
#         answer+=chr(x)
#     elif 'A'<=x and x<='Z':
#         x=ord(x)+13
#         if x>90:
#             x-=26
#         answer+=chr(x)
