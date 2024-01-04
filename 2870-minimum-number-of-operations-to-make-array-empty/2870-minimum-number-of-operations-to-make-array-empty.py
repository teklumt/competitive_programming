class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        for i in count:
            if count[i]>=3:
                if count[i]%3==0:
                    res+=count[i]//3
                    count[i]=0
                else:
                    if (count[i]%3)%2==0:
                        res+=count[i]//3
                        res+=(count[i]%3)//2
                        count[i]=0
                    else:
                        n=(count[i]//3)-1
                        res+=n
                        count[i]-=n*3
            if count[i]%2==0:
                res+=count[i]//2
                count[i]=0

            if count[i]!=0:
                return -1
        return res