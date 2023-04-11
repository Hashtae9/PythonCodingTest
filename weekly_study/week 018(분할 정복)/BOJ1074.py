# z
import sys

N, r, c = map(int, sys.stdin.readline().split())

count = 0

def divide_four(size, x, y):
    global count

    if size == 0:return

    # 1번지점
    if size//2 > x and size//2 > y:
        divide_four(size//2, x, y)

    # 2번지점
    elif size//2 > x and size//2 <= y:
        count += (size//2)*(size//2)
        divide_four(size//2, x, y-(size//2))

    # 3번지점
    elif size//2 <= x and size//2 > y:
        count += 2 * (size//2)*(size//2)
        divide_four(size//2, x-(size//2), y)

    # 4번지점
    elif size//2 <= x and size//2 <= y:
        count += 3 * (size//2)*(size//2)
        divide_four(size//2, x-(size//2), y-(size//2))

divide_four(2**N, r, c)
print(count)