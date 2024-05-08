class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = 0
        right = len(text) - 1

        cc = 0

        str1_= ""
        str2_= ""
        while left <= right:
            str1_ += text[left]
            str2_ += text[right]
            # print(str1_ , str2_)
            if str1_ == str2_[::-1]:
                if left == right:
                    cc += 1
                else:
                    cc += 2
                str1_= ""
                str2_= ""
            left += 1
            right -= 1

        if str1_ or str2_:
            cc += 1

            
            
        return cc


        