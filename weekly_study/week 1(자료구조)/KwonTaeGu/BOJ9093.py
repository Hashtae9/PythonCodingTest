#단어 뒤집기(9093번)
import sys
N = int(input())

for _ in range(N):
    str = sys.stdin.readline()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    #join
    answer = " ".join(reverse_words)
    print(answer)
