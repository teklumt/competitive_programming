class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        myhash=defaultdict(list)
        mynum=sorted(nums)
        postsum=sum(nums)
        presum=0
        n=len(nums)
        result=[]
        for i in range(n):
            if i==0:
                presum=0
                postsum-=nums[i]
                if nums[i] not in myhash:
                    myhash[nums[i]].append(presum)
                    myhash[nums[i]].append(postsum)
                    myhash[nums[i]].append(i-0)
                    myhash[nums[i]].append(n-i-1)
            elif i==n-1:
                presum+=nums[i-1]
                postsum=0
                if nums[i] not in myhash:
                    myhash[nums[i]].append(presum)
                    myhash[nums[i]].append(postsum)
                    myhash[nums[i]].append(i-0)
                    myhash[nums[i]].append(n-i-1)
            else:
                presum+=nums[i-1]
                postsum-=nums[i]
                if nums[i] not in myhash:
                    myhash[nums[i]].append(presum)
                    myhash[nums[i]].append(postsum)
                    myhash[nums[i]].append(i-0)
                    myhash[nums[i]].append(n-i-1)
        for i in nums:
            mylist=myhash[i]
            result.append((i*mylist[2]-mylist[0])+abs(i*mylist[3]-mylist[1]))
        return result