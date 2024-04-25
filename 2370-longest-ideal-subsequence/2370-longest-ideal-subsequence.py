class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ans = [0] * 26
        for char in s:
            answer = 0 
            idx = ord(char) - ord('a')
            for i in range(26):
                query_char = chr(ord('a') + i)
                if abs(ord(char) - ord(query_char)) <= k:
                    answer = max(1 + ans[i], answer) 
            ans[idx] = answer
        
        return max(ans)