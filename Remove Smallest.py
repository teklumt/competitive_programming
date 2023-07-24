n = int(input())
result = []
for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    temp = []
    for i in range(m-1):
        temp.append(abs(arr[i+1]-arr[i]))
    if len(temp) == 0:
        result.append("YES")
    elif max(temp) <= 1:
        result.append("YES")
    else:
        result.append("NO")
for i in range(len(result)):
    print(result[i])
