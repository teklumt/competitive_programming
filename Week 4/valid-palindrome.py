class Solution:
    def isPalindrome(self, s: str) -> bool:
        num=["0","1","2","3","4","5","6","7","8","9"]
        new=""
        bol=True
        for n in s:
            if n.isalpha():
                new+=n.lower()
            if n in num:
                new+=n
        # for n in range(len(new)):
        #     if new[n]!=new[-1-n]:
        #         bol=False
        #         break

        return new==new[::-1]