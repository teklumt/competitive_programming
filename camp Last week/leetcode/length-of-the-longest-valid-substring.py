class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ford = set(forbidden)
        # print(ford)
        def check(str_):
            for i in range(len(str_)):
                temp = ""
                for j in range(i ,len(str_)):

                    temp += str_[j]
                    if temp in ford:
                        # print(temp)
                        return False
            return True

        res = 0
        left = 0
        for i in range(len(word)):
            
            while left <= i and not check(word[max(i - 10 , left):i + 1]):
                left += 1
            res = max(res, i - left + 1)
        return res 


        
        # print(check("aahj"))

        
        # return 1
        # for i in word:
        #     temp.append(i)
        #     bol = True
        #     tar = 
        #     for i in