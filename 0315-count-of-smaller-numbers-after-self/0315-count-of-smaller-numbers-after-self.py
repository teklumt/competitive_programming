class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        newNum = [[nums[i], i] for i in range(len(nums))]

        res = [0] * len(nums)
        def  marge(left, right):
           
            i = 0
            j = 0
            while i < len(left):

                while j < len(right) and right[j][0] < left[i][0]:
                    
                    j+=1
                res[left[i][1]] +=  j
                i += 1

            
            return sorted(left + right)
        

        def margeSort(newNum ):
            if len(newNum) <= 1:
                return newNum
            mid = len(newNum) // 2
            left = margeSort(newNum[:mid])
            right = margeSort(newNum[mid:])
            
            return marge(left,right)
    
        margeSort(newNum)
        return res

