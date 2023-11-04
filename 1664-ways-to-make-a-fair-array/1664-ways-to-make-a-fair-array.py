class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum=0
        odd_sum=0
        count=0
        for i in range(len(nums)):
            if i%2!=0:
                odd_sum+=nums[i]
            else:
                even_sum+=nums[i]
        even_move=even_sum
        odd_move=odd_sum
        post_even=0
        post_odd=0
        pre_odd=0
        pre_even=0
        for i in range(len(nums)):
            if i==0:
                even_move-=nums[i]
                pre_even=0
                pre_odd=0
                post_even=even_move
                post_odd=odd_move
            elif i==len(nums)-1:
                if i%2!=0:
                    pre_even=even_sum
                    pre_odd=odd_sum-nums[i]
                else:
                    pre_odd=odd_sum
                    pre_even=even_sum-nums[i]
                post_even=0
                post_odd=0
            else:
                if i%2!=0:
                    odd_move-=nums[i]
                    post_even=even_move
                    pre_even=even_sum-post_even
                    post_odd=odd_move
                    pre_odd=odd_sum-post_odd-nums[i]
                else:
                    even_move-=nums[i]
                    post_odd=odd_move
                    pre_odd=odd_sum-post_odd
                    post_even=even_move
                    pre_even=even_sum-post_even-nums[i]
            
            even=post_odd + pre_even
            odd=post_even + pre_odd
            if even==odd:
                count+=1
        return count