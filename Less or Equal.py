n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k == 0:
    if min(a) == 1:
        print(-1)
    else:
        print(a[0]-1)
else:
    res = a[:k]
    if res.count(res[-1]) == a.count(a[k-1]):
        print(res[-1])
    else:
        print(-1)
