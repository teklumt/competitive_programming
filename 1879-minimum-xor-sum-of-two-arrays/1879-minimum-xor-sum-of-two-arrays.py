class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        memo = {}
        mask = 0
        m = len(nums2)
                
        def func(mask, ind):
            if ind >= len(nums1):
                return  0
            state  = (mask, ind)
            if state not in memo:
                temp = inf
                for j in range(len(nums2)):
                    if not mask & 1 << (m - j - 1):
                        mask |= 1 << (m - j - 1)
                        temp = min(temp, func(mask , ind + 1 ) + (nums1[ind] ^ nums2[j]))
                        mask ^= 1 << (m - j - 1)

                memo[state] = temp
                                       
            
            return memo[state]
        res = func(mask, 0)

        return res

            
            