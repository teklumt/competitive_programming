class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursive(r,l,player1):
            nonlocal nums
            if l>r:
                return 0    
            # if bol:
            if player1:
                score1= nums[l] + recursive(r,l+1,not player1)
                score2= nums[r] + recursive(r-1,l,not player1)
                return max(score1,score2)
            else:
                score1= -nums[l] + recursive(r,l+1,not player1)
                score2= -nums[r] + recursive(r-1,l,not player1)
                return min(score1,score2)


        return recursive(len(nums)-1,0,True)>=0