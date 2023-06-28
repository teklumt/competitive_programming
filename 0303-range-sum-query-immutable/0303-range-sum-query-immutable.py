class NumArray:

    def __init__(self, nums: List[int]):
        self.data=nums.copy()

    def sumRange(self, left: int, right: int) -> int:
        if left<=right:
            return sum(self.data[left:right+1])
                   


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)