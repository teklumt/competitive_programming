n = int(input())
result = []
for i in range(n):
    m = list(map(int, input().split()))
    result.append(m)
data = []
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == 1:
            n = []
            n.append(sorted([i+1, j+1]))
            if n not in data:
                data.append(n)

print(len(data))
