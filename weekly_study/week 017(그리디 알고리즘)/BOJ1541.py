#잃어버린 괄호
import sys

text = sys.stdin.readline().strip().split("-")

if len(text) == 1:
    print(eval(text[0]))
    exit()

result = sum(map(int, text[0].split('+')))

for i in text[1:]:
    result -= sum(map(int, i.split('+')))
print(result)