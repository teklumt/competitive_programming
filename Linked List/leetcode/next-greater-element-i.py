class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        res=[]
        stack=[]

        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1][-1]:
                num=stack.pop()
                hashmap[nums2[num[0]]]=nums2[i]
            stack.append([i,nums2[i]])
            
        for i in nums1:
            res.append(hashmap.get(i,-1))
        return res

