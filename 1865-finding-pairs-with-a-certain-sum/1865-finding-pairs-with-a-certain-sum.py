class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.data1=nums1.copy()
        self.data2=nums2.copy()
        self.COUNTER=Counter(nums2)

    def add(self, index: int, val: int) -> None:
        pre=self.data2[index]
        self.COUNTER[pre]-=1
        self.COUNTER[pre+val]+=1
        self.data2[index]+=val

    def count(self, tot: int) -> int:
        return sum(self.COUNTER[tot-x] for x in self.data1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)