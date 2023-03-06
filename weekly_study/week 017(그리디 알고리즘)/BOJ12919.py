# a와 b2
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())
check = False


def dfs(arr):
    global check
    if len(arr) == len(s):
        if arr == s:
            check = True
        return

    if t[0] == 'B':
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()

    if t[-1] == 'A':
        t.pop()
        dfs(t)
        t.append('A')
dfs(t)

if check:print(1)
else: print(0)

# baabaaaaab baaaaabaa
# baaaaaba, aabaaaaa