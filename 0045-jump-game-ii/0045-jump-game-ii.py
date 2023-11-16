class Solution:
    def jump(self, nums: List[int]) -> int:
        stack=[max(nums)+9]
        if len(nums)>1:
            for i in range(len(nums)-2,-1,-1):
                r=len(nums)-1-i
                if stack:
                    if r<=nums[i]:
                        stack.append(1)
                    else:
                        if nums[i]==1:
                            stack.append(stack[-1]+1)
                        else:
                            minn=max(stack)
                            for j in range(-1,-nums[i]-1,-1):
                                minn=min(minn,stack[j])

                            stack.append(minn+1)
                else:
                    stack.append(r)
            return stack[-1]
        else:
            return 0
