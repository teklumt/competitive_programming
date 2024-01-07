class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win=deque()
        res=0
        for i in s:
            win.append(i)
            while len(win)!=len(set(win)):
                win.popleft()
            res=max(res,len(win))
        return res
