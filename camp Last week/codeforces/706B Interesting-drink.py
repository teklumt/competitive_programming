from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
import sys
def Iint():return int(sys.stdin.readline().strip())
def Ilint():return list(map(int, sys.stdin.readline().strip().split()))
def Istring():return sys.stdin.readline().strip()


def solve():
    # pass.

    size =  Iint()
    arr = sorted(Ilint())
    nq = Iint()

    for _ in range(nq):
        q = Iint()
        ind  = bisect_right(arr, q)
    
        if ind >= len(arr):
            print(size)
        else:
            if ind == 0:
                if arr[ind] > q:
                    print(0)
                else:
                    print(1)
            else:
                if arr[ind] <= q:
                    print(ind + 1)
                else:
                    print(ind)





def main():
    t = 1

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
