class Solution:
    def checkRecord(self, s: str) -> bool:
        mylist=list(s)
        n=mylist.count('A')
        stack=[]
        len_n=0
        for i in s:
            if i=='L':
                stack.append(i)
            else:
                len_n=max(len_n,len(stack))
                stack=[]
        len_n=max(len_n,len(stack))
        return True if len_n<3 and n<2 else False