#N과 M 9
import itertools
n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
com = sorted(list(set(itertools.permutations(arr, m))))
for i in com:
    print(str(i).strip('(').strip(')').replace(',', ''))