class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res=0
        queue=deque()
        maxx=deque()
        minn=deque()
        for i in nums:
            while queue and ((minn and abs(i-minn[0])>limit) or (maxx and abs(i-maxx[0])>limit)):
                num=queue.popleft()
                if minn and num==minn[0]:minn.popleft()
                if maxx and num==maxx[0]:maxx.popleft()
            queue.append(i)
            res=max(res,len(queue))
            while minn and minn[-1]>i:
                minn.pop()
            while maxx and maxx[-1]<i:
                maxx.pop()
            maxx.append(i)
            minn.append(i)
            
        return res