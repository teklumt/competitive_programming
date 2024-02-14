t=int(input())
for _ in range(t):
    size=int(input())
    arr=list(input())
    store={0:1}
    summ=0
    res=0
    for i in range(len(arr)):
        summ+=int(arr[i])
        res+=store.get(summ-i-1,0)
        store[summ-i-1]=store.get(summ-i-1,0)+1
    print(res)

