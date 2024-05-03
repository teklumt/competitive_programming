class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        totX = nums[0]
        for i in range(1, len(nums)):
            totX ^= nums[i]
        
        res = []
        bitL = (2**maximumBit).bit_length() - 1
        for i in nums[::-1]:
            num = bin(totX)[2:] 
            if len(num) < bitL:
                num = "0" * (bitL - len(num)) + num
            elif len(num) > bitL:
                num = num[-bitL:]
            temp = []
            for j in range(len(num)):
                temp.append("1" if num[j] == '0' else '0') 
            res.append(int("".join(temp), 2))
           
            totX ^= i
        return res