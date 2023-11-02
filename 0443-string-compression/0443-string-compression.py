class Solution:
    def compress(self, chars: List[str]) -> int:
        stack=[]
        count=1
        res=[]
        for j in range(len(chars)):
            if stack:
                if chars[j] in stack:
                    count+=1
                else:
                    res.append(stack[-1])
                    if count>1:
                        res.append(str(count))
                    
                    count=1
                    stack=[chars[j]]
            else:
                stack.append(chars[j])
        if stack:
            res.append(stack[-1])
            if count>1:
                res.append(str(count))
        res=list("".join(res))
        chars[:] = res
        return len(res)
