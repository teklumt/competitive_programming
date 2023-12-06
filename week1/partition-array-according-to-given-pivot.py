class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        large=[]
        equal=[]
        small=[]
        for i in nums:
            if i>pivot:
                large.append(i)
            elif i<pivot:
                small.append(i)
            else:
                equal.append(i)
                
        return small + equal + large