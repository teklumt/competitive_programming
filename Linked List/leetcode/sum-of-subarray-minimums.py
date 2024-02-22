class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
       
        stack=[]
        res=0
        
        for i in range(len(arr)+1):
            while stack and (i==len(arr)  or arr[stack[-1]]>=arr[i]):
                curr=stack.pop()
                left= stack[-1] if stack else -1
                right=i

                count=(curr-left) * (right-curr)%(10**9 + 7)

                res+=(count*arr[curr])
               
            stack.append(i)
        return res%(10**9 + 7)



