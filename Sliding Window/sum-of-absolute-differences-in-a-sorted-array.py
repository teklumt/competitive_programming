class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        presum=[0]
        postsum=[0]
        res=[]
        for i in nums:
            presum.append(presum[-1]+i)
        for i in range(len(nums)-1,-1,-1):
            postsum.append(postsum[-1]+nums[i])
        postsum=postsum[::-1]
        for i in range(len(nums)):
            res.append((nums[i]*i-presum[i])+abs(nums[i]*(len(nums)-1-i)-postsum[i+1]))
        return res




        
        # myhash=defaultdict(list)
        # mynum=sorted(nums)
        # postsum=sum(nums)
        # presum=0
        # n=len(nums)
        # result=[]
        # for i in range(n):
        #     if i==0:
        #         presum=0
        #         postsum-=nums[i]
        #         if nums[i] not in myhash:
        #             myhash[nums[i]].append(presum)
        #             myhash[nums[i]].append(postsum)
        #             myhash[nums[i]].append(i-0)
        #             myhash[nums[i]].append(n-i-1)
        #     elif i==n-1:
        #         presum+=nums[i-1]
        #         postsum=0
        #         if nums[i] not in myhash:
        #             myhash[nums[i]].append(presum)
        #             myhash[nums[i]].append(postsum)
        #             myhash[nums[i]].append(i-0)
        #             myhash[nums[i]].append(n-i-1)
        #     else:
        #         presum+=nums[i-1]
        #         postsum-=nums[i]
        #         if nums[i] not in myhash:
        #             myhash[nums[i]].append(presum)
        #             myhash[nums[i]].append(postsum)
        #             myhash[nums[i]].append(i-0)
        #             myhash[nums[i]].append(n-i-1)
        # print(myhash)
        
        # for i in nums:
        #     mylist=myhash[i]
        #     result.append((i*mylist[2]-mylist[0])+abs(i*mylist[3]-mylist[1]))
        # return result