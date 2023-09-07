n = int(input())
result = []
for i in range(n):
    m = list(map(int, input().split()))
    result.append(m)
data = []
for i in range(len(result)):
    check = []
    check.append(result[i].count(1))
    for j in range(len(result[i])):
        if result[i][j] == 1:
            check.append(j+1)
    data.append(check)
for i in range(len(data)):
    for j in range(len(data[i])):
        if j < len(data[i])-1:
            print(data[i][j], end=" ")
        else:
            print(data[i][j])
