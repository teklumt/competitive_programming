class Solution:
    def maxProduct(self, words: List[str]) -> int:
        check = []
        for i in words:
            curr = 0
            for j in i:
                curr |= 1 << (ord(j) - 97)
            check.append([curr, len(i)])
        maxx = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not check[i][0] & check[j][0]:
                    maxx = max(maxx,  check[i][1] * check[j][1] )
        
        return maxx
                


