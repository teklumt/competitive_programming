if __name__ == '__main__':
    N = int(input())
    result=[]
    for i in range(N):
        num =list(map(str,input().split()))
        if num[0]=="insert":
            result.insert(int(num[1]),int(num[2]))
        elif num[0]=="print":
            print(result)
        elif num[0]=="remove":
            result.remove(int(num[1]))
        elif num[0]=="append":
            result.append(int(num[1]))
        elif num[0]=="sort":
            result.sort()
        elif num[0]=="pop":
            result.pop()
        elif num[0]=="reverse":
            result.reverse()
            
